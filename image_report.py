#!/usr/bin/env python3
"""
Generate a summary report of the image updates
"""

import os
import re

def generate_image_update_report():
    """Generate a report of all image updates"""
    content_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/content"
    
    archie_files = []
    for filename in os.listdir(content_dir):
        if filename.startswith('archie-') and filename.endswith('.md'):
            archie_files.append(filename)
    
    archie_files.sort()
    
    print("📸 Image Update Report")
    print("=" * 50)
    print(f"Total Archie files updated: {len(archie_files)}")
    print()
    
    unique_images = set()
    
    for filename in archie_files[:10]:  # Show first 10 as examples
        filepath = os.path.join(content_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            image_match = re.search(r'image: "([^"]*)"', content)
            title_match = re.search(r'title: ([^\n]*)', content)
            
            if image_match and title_match:
                image_path = image_match.group(1)
                title = title_match.group(1).strip()
                unique_images.add(image_path)
                print(f"✅ {filename}")
                print(f"   Title: {title}")
                print(f"   Image: {image_path}")
                print()
                
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")
    
    if len(archie_files) > 10:
        print(f"... and {len(archie_files) - 10} more files")
        print()
    
    print(f"📊 Summary:")
    print(f"   • Files updated: {len(archie_files)}")
    print(f"   • Unique images used: {len(unique_images)}")
    print(f"   • Default image fallbacks: {sum(1 for img in unique_images if 'img-509195' in img)}")
    print(f"   • Custom images: {len(unique_images) - sum(1 for img in unique_images if 'img-509195' in img)}")

if __name__ == "__main__":
    generate_image_update_report()