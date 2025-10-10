#!/usr/bin/env python3

import os
import re
import glob

def fix_yaml_frontmatter(file_path):
    """Fix YAML frontmatter issues in a markdown file."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split the content into frontmatter and body
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    frontmatter = parts[1].strip()
    body = parts[2]
    
    # Fix common YAML issues
    lines = frontmatter.split('\n')
    fixed_lines = []
    
    for line in lines:
        if line.strip():
            # Ensure proper spacing after colons
            if ':' in line and not line.strip().startswith('#'):
                key_part, value_part = line.split(':', 1)
                # Clean up the value part - remove extra spaces and ensure single space after colon
                value_part = value_part.strip()
                if value_part:
                    fixed_line = f"{key_part}: {value_part}"
                else:
                    fixed_line = f"{key_part}:"
                fixed_lines.append(fixed_line)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    # Reconstruct the content
    new_content = f"---\n{chr(10).join(fixed_lines)}\n---{body}"
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    # Get all markdown files
    md_files = glob.glob('/Users/neilhaddley/Documents/GitHub/haddley.github.io/content/*.md')
    
    print(f"Found {len(md_files)} markdown files to process...")
    
    fixed_count = 0
    for file_path in md_files:
        try:
            if fix_yaml_frontmatter(file_path):
                fixed_count += 1
                print(f"Fixed: {os.path.basename(file_path)}")
        except Exception as e:
            print(f"Error processing {os.path.basename(file_path)}: {e}")
    
    print(f"\nCompleted! Fixed {fixed_count} files.")

if __name__ == "__main__":
    main()