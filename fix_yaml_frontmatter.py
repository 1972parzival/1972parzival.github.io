#!/usr/bin/env python3

import os
import re
import yaml
from pathlib import Path

def fix_yaml_frontmatter(file_path):
    """Fix YAML frontmatter issues in markdown files"""
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
        
        # Common fixes for YAML issues
        fixes_made = []
        
        # Fix 1: Quote image paths that contain spaces or special characters
        image_pattern = r'^(\s*image:\s*)([^"\n]+\s[^"\n]*\.(jpg|jpeg|png|gif|webp|svg))\s*$'
        def quote_image_path(match):
            indent = match.group(1)
            path = match.group(2).strip()
            if not (path.startswith('"') and path.endswith('"')):
                fixes_made.append(f"Quoted image path: {path}")
                return f'{indent}"{path}"'
            return match.group(0)
        
        frontmatter = re.sub(image_pattern, quote_image_path, frontmatter, flags=re.MULTILINE | re.IGNORECASE)
        
        # Fix 2: Handle multiline values that aren't properly formatted
        # Look for lines that might be continuation of previous values
        lines = frontmatter.split('\n')
        fixed_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check if this line looks like a YAML key: value pair
            if ':' in line and not line.strip().startswith('#'):
                key_match = re.match(r'^(\s*)([^:]+):\s*(.*)$', line)
                if key_match:
                    indent, key, value = key_match.groups()
                    
                    # If value contains problematic patterns, quote it
                    if value and not value.startswith('"') and not value.startswith("'"):
                        # Check for spaces in file extensions or problematic characters
                        if re.search(r'\.\s+(jpg|jpeg|png|gif|webp|svg)', value, re.IGNORECASE):
                            fixes_made.append(f"Fixed spaced extension in: {key}")
                            value = f'"{value.strip()}"'
                        elif ' ' in value and any(ext in value.lower() for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']):
                            fixes_made.append(f"Quoted image path with spaces: {key}")
                            value = f'"{value.strip()}"'
                    
                    fixed_lines.append(f"{indent}{key}: {value}")
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)
            i += 1
        
        frontmatter = '\n'.join(fixed_lines)
        
        # Fix 3: Handle specific problematic patterns we saw in the errors
        # Fix "Vi." pattern that seems to be causing issues
        frontmatter = re.sub(r':\s*Vi\.\s*$', ': "Vi."', frontmatter, flags=re.MULTILINE)
        
        # Fix 4: Ensure proper spacing around colons
        frontmatter = re.sub(r'^(\s*)([^:\s]+):\s*([^"\n].*)$', lambda m: f"{m.group(1)}{m.group(2)}: {m.group(3)}", frontmatter, flags=re.MULTILINE)
        
        # Try to parse the fixed YAML to ensure it's valid
        try:
            yaml.safe_load(frontmatter)
        except yaml.YAMLError as e:
            return False, f"YAML still invalid after fixes: {str(e)}"
        
        # Write back the fixed content
        if fixes_made:
            new_content = f"---\n{frontmatter}\n---{body}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, f"Fixed: {', '.join(fixes_made)}"
        
        return False, "No fixes needed"
        
    except Exception as e:
        return False, f"Error processing file: {str(e)}"

def main():
    """Fix YAML frontmatter issues in all markdown files"""
    content_dir = Path("content")
    
    if not content_dir.exists():
        print("Content directory not found!")
        return
    
    total_files = 0
    fixed_files = 0
    
    print("🔧 Fixing YAML frontmatter issues...")
    print("=" * 50)
    
    # Process all .md files
    for md_file in content_dir.rglob("*.md"):
        total_files += 1
        success, message = fix_yaml_frontmatter(md_file)
        
        if success:
            fixed_files += 1
            print(f"✅ {md_file.name}: {message}")
        elif "No frontmatter" not in message and "No fixes needed" not in message:
            print(f"❌ {md_file.name}: {message}")
    
    print("\n" + "=" * 50)
    print(f"📊 Summary:")
    print(f"   Total files processed: {total_files}")
    print(f"   Files fixed: {fixed_files}")
    print(f"   Success rate: {(fixed_files/total_files)*100:.1f}%")

if __name__ == "__main__":
    main()