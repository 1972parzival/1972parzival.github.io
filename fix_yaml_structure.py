#!/usr/bin/env python3

import os
import re
from pathlib import Path

def fix_yaml_structure(file_path):
    """Fix YAML frontmatter structural issues in markdown files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has frontmatter
        if not content.startswith('---'):
            return False, "No frontmatter found"
        
        # Split frontmatter and content
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False, "Invalid frontmatter structure"
        
        frontmatter = parts[1].strip()
        body = parts[2]
        
        fixes_made = []
        original_frontmatter = frontmatter
        
        # Fix 1: Fix categories array format
        # Look for broken categories format like:
        # categories:
        # - Personal
        # - Projects
        
        # Replace multi-line categories with proper single-line format
        categories_pattern = r'categories:\s*\n(?:\s*-\s*([^\n]+)\n?)+'
        def fix_categories(match):
            full_match = match.group(0)
            # Extract all category items
            category_items = re.findall(r'-\s*([^\n]+)', full_match)
            if category_items:
                # Clean up category names
                clean_categories = [cat.strip() for cat in category_items if cat.strip()]
                if len(clean_categories) == 1:
                    fixes_made.append(f"Fixed single category format")
                    return f"categories: [{clean_categories[0]}]"
                else:
                    fixes_made.append(f"Fixed multiple categories format")
                    return f"categories: [{', '.join(clean_categories)}]"
            return match.group(0)
        
        frontmatter = re.sub(categories_pattern, fix_categories, frontmatter, flags=re.MULTILINE)
        
        # Fix 2: Fix multi-line description format
        # description: This is a project i've been wanting to do since near the end of last
        # year (2023), but only now after a lot of research and smaller projects do i feel
        # comfortable to pursue it. This project is creat.
        
        description_pattern = r'description:\s*([^\n]+(?:\n[^a-zA-Z:\n]+[^\n]*)*)'
        def fix_description(match):
            desc_text = match.group(1)
            # Join all lines and clean up
            clean_desc = ' '.join(line.strip() for line in desc_text.split('\n') if line.strip())
            if '\n' in desc_text:
                fixes_made.append("Fixed multi-line description")
            return f'description: "{clean_desc}"'
        
        frontmatter = re.sub(description_pattern, fix_description, frontmatter, flags=re.MULTILINE)
        
        # Fix 3: Quote image paths with spaces
        image_pattern = r'^(\s*image:\s*)([^"\n]+\s[^"\n]*\.(jpg|jpeg|png|gif|webp|svg))\s*$'
        def quote_image_path(match):
            indent = match.group(1)
            path = match.group(2).strip()
            if not (path.startswith('"') and path.endswith('"')):
                fixes_made.append(f"Quoted image path with spaces")
                return f'{indent}"{path}"'
            return match.group(0)
        
        frontmatter = re.sub(image_pattern, quote_image_path, frontmatter, flags=re.MULTILINE | re.IGNORECASE)
        
        # Fix 4: Remove extra blank lines and normalize spacing
        lines = frontmatter.split('\n')
        cleaned_lines = []
        for line in lines:
            if line.strip():  # Keep non-empty lines
                cleaned_lines.append(line.rstrip())
        
        frontmatter = '\n'.join(cleaned_lines)
        
        # Fix 5: Ensure proper YAML key-value format
        frontmatter = re.sub(r'^(\s*)([^:\s]+):\s*$', r'\1\2: ""', frontmatter, flags=re.MULTILINE)
        
        # Write back the fixed content if changes were made
        if frontmatter != original_frontmatter:
            if not fixes_made:
                fixes_made.append("General formatting fixes")
            
            new_content = f"---\n{frontmatter}\n---{body}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, f"Fixed: {', '.join(fixes_made)}"
        
        return False, "No fixes needed"
        
    except Exception as e:
        return False, f"Error processing file: {str(e)}"

def main():
    """Fix YAML frontmatter structural issues in all markdown files"""
    content_dir = Path("content")
    
    if not content_dir.exists():
        print("Content directory not found!")
        return
    
    total_files = 0
    fixed_files = 0
    
    print("🔧 Fixing YAML frontmatter structural issues...")
    print("=" * 60)
    
    # Process all .md files
    for md_file in content_dir.rglob("*.md"):
        total_files += 1
        success, message = fix_yaml_structure(md_file)
        
        if success:
            fixed_files += 1
            print(f"✅ {md_file.name}: {message}")
        elif "No frontmatter" not in message and "No fixes needed" not in message:
            print(f"❌ {md_file.name}: {message}")
    
    print("\n" + "=" * 60)
    print(f"📊 Summary:")
    print(f"   Total files processed: {total_files}")
    print(f"   Files fixed: {fixed_files}")
    print(f"   Success rate: {(fixed_files/total_files)*100:.1f}%")

if __name__ == "__main__":
    main()