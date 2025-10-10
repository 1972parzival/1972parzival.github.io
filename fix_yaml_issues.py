#!/usr/bin/env python3
"""
Fix YAML frontmatter issues in converted markdown files
"""

import os
import re
import yaml

def fix_yaml_frontmatter(file_path):
    """Fix YAML frontmatter issues in a markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split frontmatter and content
        if not content.startswith('---'):
            return False
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False
        
        frontmatter_str = parts[1].strip()
        body_content = parts[2]
        
        # Parse the YAML to detect issues
        try:
            frontmatter = yaml.safe_load(frontmatter_str)
        except yaml.YAMLError as e:
            print(f"YAML error in {file_path}: {e}")
            return False
        
        # Clean up the frontmatter
        if 'description' in frontmatter:
            desc = frontmatter['description']
            if desc:
                # Remove quotes and escape problematic characters
                desc = str(desc).strip()
                # Remove line breaks and extra whitespace
                desc = ' '.join(desc.split())
                # Limit length to avoid issues
                if len(desc) > 200:
                    desc = desc[:197] + "..."
                # Escape quotes
                desc = desc.replace('"', '\\"')
                frontmatter['description'] = desc
            else:
                frontmatter['description'] = "Content from Archie's website"
        
        if 'title' in frontmatter:
            title = frontmatter['title']
            if title:
                title = str(title).strip()
                # Remove line breaks and extra whitespace
                title = ' '.join(title.split())
                # Escape quotes
                title = title.replace('"', '\\"')
                frontmatter['title'] = title
        
        # Reconstruct the file
        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        new_content = f"---\n{new_frontmatter}---{body_content}"
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Fixed: {os.path.basename(file_path)}")
        return True
        
    except Exception as e:
        print(f"Error fixing {file_path}: {str(e)}")
        return False

def main():
    content_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/content"
    
    print("Fixing YAML frontmatter issues...")
    
    fixed_count = 0
    for filename in os.listdir(content_dir):
        if filename.startswith('archie-') and filename.endswith('.md'):
            file_path = os.path.join(content_dir, filename)
            if fix_yaml_frontmatter(file_path):
                fixed_count += 1
    
    print(f"\nFixed {fixed_count} files")

if __name__ == "__main__":
    main()