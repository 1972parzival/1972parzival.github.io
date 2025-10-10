#!/usr/bin/env python3
"""
Update image properties in markdown files to match the first meaningful image from corresponding HTML files
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_first_image_from_html(html_file_path):
    """Extract the first meaningful image from an HTML file"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove navigation sections to avoid getting nav logos
        for nav in soup.find_all(['nav', 'section'], class_=lambda x: x and 'menu' in str(x)):
            nav.decompose()
        
        # Look for meaningful images (not icons, logos, or very small images)
        images = soup.find_all('img')
        
        for img in images:
            src = img.get('src', '')
            alt = img.get('alt', '')
            
            # Skip if no src
            if not src:
                continue
                
            # Convert relative path to absolute
            if src.startswith('assets/'):
                src = '/' + src
            
            # Skip common logo/icon files and small images
            if any(skip in src.lower() for skip in ['logo', 'icon', 'favicon', 'img-509195']):
                continue
            
            # Skip if it's clearly a navigation or header image
            parent_classes = []
            parent = img.parent
            while parent and parent.name:
                if parent.get('class'):
                    parent_classes.extend(parent.get('class'))
                parent = parent.parent
            
            if any(nav_class in str(parent_classes).lower() for nav_class in ['menu', 'nav', 'header']):
                continue
            
            # This looks like a meaningful content image
            return src
        
        # If no meaningful image found, return default
        return "/assets/images/img-509195-1076x1068.png"
        
    except Exception as e:
        print(f"Error extracting image from {html_file_path}: {str(e)}")
        return "/assets/images/img-509195-1076x1068.png"

def update_markdown_image(md_file_path, new_image_path):
    """Update the image property in a markdown file's frontmatter"""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split frontmatter and content
        if not content.startswith('---'):
            return False
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False
        
        frontmatter = parts[1]
        body_content = parts[2]
        
        # Update the image line
        lines = frontmatter.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('image:'):
                lines[i] = f'image: "{new_image_path}"'
                break
        
        # Reconstruct the file
        new_frontmatter = '\n'.join(lines)
        new_content = f"---{new_frontmatter}---{body_content}"
        
        # Write back to file
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"Error updating {md_file_path}: {str(e)}")
        return False

def main():
    archie_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/Archie/1972parzival.github.io"
    content_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/content"
    
    print("Updating markdown image properties to match HTML files...")
    
    # Create mapping of HTML files to markdown files
    html_to_md_mapping = {
        'index.html': 'archie-home.md',
        'aii3.html': 'aii3.md',
        'beepbox.html': 'beepbox.md'
    }
    
    # Add page mappings
    for i in range(1, 68):
        html_to_md_mapping[f'page{i}.html'] = f'archie-page-{i}.md'
    
    updated_count = 0
    
    for html_file, md_file in html_to_md_mapping.items():
        html_path = os.path.join(archie_dir, html_file)
        md_path = os.path.join(content_dir, md_file)
        
        if os.path.exists(html_path) and os.path.exists(md_path):
            # Extract first meaningful image from HTML
            first_image = extract_first_image_from_html(html_path)
            
            # Update markdown file
            if update_markdown_image(md_path, first_image):
                print(f"Updated {md_file}: {first_image}")
                updated_count += 1
            else:
                print(f"Failed to update {md_file}")
        else:
            if not os.path.exists(html_path):
                print(f"HTML file not found: {html_file}")
            if not os.path.exists(md_path):
                print(f"Markdown file not found: {md_file}")
    
    print(f"\nUpdated {updated_count} markdown files with new image properties")

if __name__ == "__main__":
    main()