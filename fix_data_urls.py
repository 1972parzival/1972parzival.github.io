#!/usr/bin/env python3
"""
Fix remaining image issues and provide fallback images for data URLs
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def get_better_fallback_image(html_file_path):
    """Get a better fallback image by looking for any meaningful image in the HTML"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Look for ANY images that aren't data URLs or logos
        images = soup.find_all('img')
        
        for img in images:
            src = img.get('src', '')
            
            if not src or src.startswith('data:'):
                continue
                
            # Convert relative path to absolute
            if src.startswith('assets/'):
                src = '/' + src
            
            # Skip obvious logos but be less strict
            if 'img-509195' in src:
                continue
            
            # Return the first reasonable image found
            return src
        
        # If still no image found, return default
        return "/assets/images/img-509195-1076x1068.png"
        
    except Exception as e:
        print(f"Error getting fallback image from {html_file_path}: {str(e)}")
        return "/assets/images/img-509195-1076x1068.png"

def fix_data_url_images():
    """Fix markdown files that have data URL images"""
    archie_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/Archie/1972parzival.github.io"
    content_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/content"
    
    # Files that had data URLs
    problem_files = [
        ('index.html', 'archie-home.md'),
        ('page1.html', 'archie-page-1.md'),
        ('page10.html', 'archie-page-10.md'),
        ('page14.html', 'archie-page-14.md'),
        ('page20.html', 'archie-page-20.md'),
        ('page24.html', 'archie-page-24.md'),
        ('page50.html', 'archie-page-50.md'),
        ('page57.html', 'archie-page-57.md')
    ]
    
    fixed_count = 0
    
    for html_file, md_file in problem_files:
        html_path = os.path.join(archie_dir, html_file)
        md_path = os.path.join(content_dir, md_file)
        
        if os.path.exists(html_path) and os.path.exists(md_path):
            # Get a better fallback image
            better_image = get_better_fallback_image(html_path)
            
            # Update the markdown file
            try:
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace the data URL image with better image
                updated_content = re.sub(
                    r'image: "data:image/gif;base64,[^"]*"',
                    f'image: "{better_image}"',
                    content
                )
                
                if updated_content != content:
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    
                    print(f"Fixed {md_file}: {better_image}")
                    fixed_count += 1
                
            except Exception as e:
                print(f"Error fixing {md_file}: {str(e)}")
    
    print(f"\nFixed {fixed_count} files with data URL images")

def verify_results():
    """Verify the results by checking a few sample files"""
    content_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/content"
    
    sample_files = ['archie-home.md', 'archie-page-4.md', 'archie-page-5.md']
    
    for filename in sample_files:
        filepath = os.path.join(content_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract image line
            image_match = re.search(r'image: "([^"]*)"', content)
            if image_match:
                print(f"{filename}: {image_match.group(1)}")

if __name__ == "__main__":
    print("Fixing data URL images...")
    fix_data_url_images()
    
    print("\nVerifying sample results:")
    verify_results()