#!/usr/bin/env python3

import os
import re
import glob
from categorization_mapping import CATEGORY_MAPPING

def update_categories_in_file(file_path):
    """Update categories in a markdown file."""
    
    # Get the slug from filename
    filename = os.path.basename(file_path)
    slug = filename.replace('.md', '')
    
    # Get new categories
    new_categories = CATEGORY_MAPPING.get(slug, ['Personal', 'Projects'])
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has frontmatter
    if not content.startswith('---'):
        print(f"Warning: {filename} doesn't have frontmatter")
        return False
    
    # Split content into frontmatter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"Warning: {filename} has malformed frontmatter")
        return False
    
    frontmatter = parts[1].strip()
    body = parts[2]
    
    # Update categories line
    lines = frontmatter.split('\n')
    updated_lines = []
    categories_updated = False
    
    for line in lines:
        if line.startswith('categories:'):
            # Replace the categories line
            categories_str = '[' + ', '.join(f'"{cat}"' for cat in new_categories) + ']'
            updated_lines.append(f'categories: {categories_str}')
            categories_updated = True
        else:
            updated_lines.append(line)
    
    if not categories_updated:
        print(f"Warning: No categories line found in {filename}")
        return False
    
    # Reconstruct content
    new_content = f"---\n{chr(10).join(updated_lines)}\n---{body}"
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    # Get all markdown files
    content_dir = '/Users/neilhaddley/Documents/GitHub/haddley.github.io/content'
    md_files = glob.glob(os.path.join(content_dir, '*.md'))
    
    print(f"Found {len(md_files)} markdown files to update...")
    
    # Group files by their new categories for reporting
    category_groups = {}
    updated_count = 0
    
    for file_path in md_files:
        filename = os.path.basename(file_path)
        slug = filename.replace('.md', '')
        new_categories = CATEGORY_MAPPING.get(slug, ['Personal', 'Projects'])
        
        # Group for reporting
        main_category = new_categories[0]
        if main_category not in category_groups:
            category_groups[main_category] = []
        category_groups[main_category].append(filename)
        
        try:
            if update_categories_in_file(file_path):
                updated_count += 1
                print(f"✅ Updated: {filename} → {new_categories}")
            else:
                print(f"❌ Failed: {filename}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
    
    print(f"\n🎉 Successfully updated {updated_count} files!")
    
    # Print summary by category
    print("\n📊 Files by Primary Category:")
    print("=" * 40)
    for category, files in sorted(category_groups.items()):
        print(f"\n{category} ({len(files)} files):")
        for filename in sorted(files):
            print(f"  • {filename}")

if __name__ == "__main__":
    main()