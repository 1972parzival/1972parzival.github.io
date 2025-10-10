#!/usr/bin/env python3
"""
Extract thumbnail mappings from page4.html and update markdown files with correct image properties.
This script reads page4.html to get the correct image-to-page mappings.
"""

import os
import re
import yaml
from bs4 import BeautifulSoup

def extract_thumbnail_mappings(page4_path):
    """Extract thumbnail image to page mappings from page4.html"""
    with open(page4_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    mappings = {}
    
    # Find all gallery items (note: the HTML has a Cyrillic 'с' instead of 'c' in the class)
    items = soup.find_all('div', class_=lambda value: value and 'item features-image' in value)
    
    print(f"Found {len(items)} gallery items")
    
    for item in items:
        # Get the image source
        img_tag = item.find('img')
        if not img_tag or not img_tag.get('src'):
            continue
            
        img_src = img_tag['src']
        # Remove assets/images/ prefix
        if img_src.startswith('assets/images/'):
            img_src = img_src[14:]  # Remove "assets/images/"
        
        # Get the linked page
        link_tag = item.find('a', href=True)
        if not link_tag:
            continue
            
        page_href = link_tag['href']
        
        # Extract page number from href (e.g., "page6.html" -> "6")
        page_match = re.search(r'page(\d+)\.html', page_href)
        if not page_match:
            continue
            
        page_num = page_match.group(1)
        
        # Get the title for verification
        title_tag = item.find('h5', class_='item-title')
        title = title_tag.get_text(strip=True) if title_tag else "Unknown"
        
        mappings[page_num] = {
            'image': img_src,
            'title': title,
            'page_file': page_href
        }
        
        print(f"Page {page_num}: {img_src} -> {title}")
    
    return mappings

def update_markdown_files(content_dir, mappings):
    """Update markdown files with correct image properties from thumbnails"""
    updated_files = []
    
    for filename in os.listdir(content_dir):
        if not filename.startswith('archie-page-') or not filename.endswith('.md'):
            continue
            
        # Extract page number from filename
        page_match = re.search(r'archie-page-(\d+)\.md', filename)
        if not page_match:
            continue
            
        page_num = page_match.group(1)
        
        if page_num not in mappings:
            print(f"Warning: No mapping found for page {page_num}")
            continue
            
        filepath = os.path.join(content_dir, filename)
        
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split frontmatter and content
        if not content.startswith('---'):
            print(f"Warning: {filename} doesn't start with frontmatter")
            continue
            
        parts = content.split('---', 2)
        if len(parts) != 3:
            print(f"Warning: Invalid frontmatter in {filename}")
            continue
            
        frontmatter_str = parts[1]
        body_content = parts[2]
        
        # Parse frontmatter
        try:
            frontmatter = yaml.safe_load(frontmatter_str)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML in {filename}: {e}")
            continue
        
        # Update image property
        mapping = mappings[page_num]
        old_image = frontmatter.get('image', 'Unknown')
        frontmatter['image'] = f"/assets/images/{mapping['image']}"
        
        print(f"Updated {filename}: {old_image} -> {frontmatter['image']}")
        
        # Write back to file
        try:
            new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
            new_content = f"---\n{new_frontmatter}---{body_content}"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            updated_files.append(filename)
            
        except Exception as e:
            print(f"Error writing {filename}: {e}")
    
    return updated_files

def main():
    # Paths
    archie_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/Archie/1972parzival.github.io"
    page4_path = os.path.join(archie_dir, "page4.html")
    content_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/content"
    
    if not os.path.exists(page4_path):
        print(f"Error: {page4_path} not found")
        return
        
    if not os.path.exists(content_dir):
        print(f"Error: {content_dir} not found")
        return
    
    print("Extracting thumbnail mappings from page4.html...")
    mappings = extract_thumbnail_mappings(page4_path)
    
    print(f"\nFound {len(mappings)} mappings")
    
    print("\nUpdating markdown files...")
    updated_files = update_markdown_files(content_dir, mappings)
    
    print(f"\nUpdated {len(updated_files)} files:")
    for filename in updated_files:
        print(f"  - {filename}")

if __name__ == "__main__":
    main()