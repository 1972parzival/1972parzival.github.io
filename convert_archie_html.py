#!/usr/bin/env python3
"""
Convert HTML files from Archie folder to Markdown format for Next.js blog
"""

import os
import re
import html
from pathlib import Path
from bs4 import BeautifulSoup
import shutil
from datetime import datetime

def extract_title_from_html(soup):
    """Extract title from HTML - try title tag first, then h1, then filename"""
    title_tag = soup.find('title')
    if title_tag and title_tag.text.strip() and title_tag.text.strip() != "Home":
        return title_tag.text.strip()
    
    h1_tag = soup.find('h1')
    if h1_tag:
        # Clean up the h1 text
        text = h1_tag.get_text().strip()
        # Remove extra whitespace and line breaks
        text = ' '.join(text.split())
        return text
    
    return None

def extract_description_from_html(soup):
    """Extract description from meta tag or first paragraph"""
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc and meta_desc.get('content'):
        return meta_desc.get('content').strip()
    
    # Try to get first meaningful paragraph
    paragraphs = soup.find_all('p', class_='mbr-text')
    for p in paragraphs:
        text = p.get_text().strip()
        if len(text) > 20:  # Only use substantial paragraphs
            return text[:200] + "..." if len(text) > 200 else text
    
    return "Content from Archie's website"

def clean_html_content(soup):
    """Extract and clean the main content from HTML"""
    # Remove navigation, scripts, styles
    for element in soup(['nav', 'script', 'style', 'meta', 'link', 'head']):
        element.decompose()
    
    # Find main content sections
    content_sections = []
    
    # Look for main content areas
    sections = soup.find_all('section')
    for section in sections:
        # Skip menu sections
        if 'menu' in section.get('class', []):
            continue
            
        section_content = []
        
        # Extract headings
        for heading in section.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            level = int(heading.name[1])
            text = heading.get_text().strip()
            if text:
                section_content.append('#' * level + ' ' + text)
        
        # Extract paragraphs
        for p in section.find_all('p'):
            text = p.get_text().strip()
            if text and len(text) > 10:  # Skip very short paragraphs
                section_content.append(text)
        
        # Extract images
        for img in section.find_all('img'):
            src = img.get('src', '')
            alt = img.get('alt', '')
            if src and not src.startswith('data:'):
                # Convert relative paths to absolute paths for assets
                if src.startswith('assets/'):
                    src = '/' + src
                section_content.append(f'![{alt}]({src})')
        
        # Extract lists
        for ul in section.find_all('ul'):
            for li in ul.find_all('li'):
                text = li.get_text().strip()
                if text:
                    section_content.append(f'- {text}')
        
        if section_content:
            content_sections.extend(section_content)
            content_sections.append('')  # Add spacing between sections
    
    return '\n\n'.join(content_sections)

def html_to_markdown(html_file_path, output_dir):
    """Convert a single HTML file to Markdown"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract metadata
        title = extract_title_from_html(soup)
        description = extract_description_from_html(soup)
        
        # Generate filename and slug
        filename = Path(html_file_path).stem
        if filename == 'index':
            title = title or "Archie Haddley Morris"
            slug = "archie-home"
        else:
            slug = filename.replace('page', 'archie-page-')
        
        # If no title found, create one from filename
        if not title:
            if filename == 'index':
                title = "Home"
            else:
                title = f"Page {filename.replace('page', '')}" if filename.startswith('page') else filename.title()
        
        # Extract main content
        content = clean_html_content(soup)
        
        # Create frontmatter
        current_date = datetime.now().strftime("%Y-%m-%d")
        frontmatter = f"""---
title: "{title}"
description: "{description}"
date: "{current_date}"
categories: ["Personal","Projects"]
tags: []
slug: "{slug}"
image: "/assets/images/img-509195-1076x1068.png"
---

"""
        
        # Combine frontmatter and content
        markdown_content = frontmatter + content
        
        # Write to output file
        output_file = os.path.join(output_dir, f"{slug}.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"Converted: {filename}.html -> {slug}.md")
        return True
        
    except Exception as e:
        print(f"Error converting {html_file_path}: {str(e)}")
        return False

def copy_images(source_dir, dest_dir):
    """Copy all images from source to destination"""
    source_images = Path(source_dir) / "assets" / "images"
    dest_images = Path(dest_dir) / "assets" / "images"
    
    # Create destination if it doesn't exist
    dest_images.mkdir(parents=True, exist_ok=True)
    
    if not source_images.exists():
        print(f"Source images directory not found: {source_images}")
        return False
    
    copied_count = 0
    for image_file in source_images.glob("*"):
        if image_file.is_file() and image_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']:
            dest_file = dest_images / image_file.name
            try:
                shutil.copy2(image_file, dest_file)
                copied_count += 1
            except Exception as e:
                print(f"Error copying {image_file.name}: {str(e)}")
    
    print(f"Copied {copied_count} images to {dest_images}")
    return True

def main():
    # Paths
    archie_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/Archie/1972parzival.github.io"
    content_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/content"
    project_root = "/Users/neilhaddley/Documents/GitHub/haddley.github.io"
    
    print("Starting conversion of Archie HTML files to Markdown...")
    
    # Copy images first
    print("\n1. Copying images...")
    copy_images(archie_dir, project_root)
    
    # Convert HTML files
    print("\n2. Converting HTML files...")
    html_files = []
    
    # Get all HTML files
    for file in os.listdir(archie_dir):
        if file.endswith('.html'):
            html_files.append(os.path.join(archie_dir, file))
    
    html_files.sort()  # Process in order
    
    converted_count = 0
    for html_file in html_files:
        if html_to_markdown(html_file, content_dir):
            converted_count += 1
    
    print(f"\nConversion complete!")
    print(f"Converted {converted_count} HTML files to Markdown")
    print(f"Files saved to: {content_dir}")

if __name__ == "__main__":
    main()