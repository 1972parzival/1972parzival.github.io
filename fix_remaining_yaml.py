#!/usr/bin/env python3
"""
Manual fix for the remaining YAML frontmatter issues
"""

import os
import re

def fix_specific_yaml_issues():
    """Fix specific YAML issues that couldn't be automatically resolved"""
    content_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/content"
    
    problematic_files = [
        'archie-page-23.md',
        'archie-page-30.md', 
        'archie-page-41.md',
        'archie-page-44.md',
        'archie-page-51.md',
        'archie-page-52.md',
        'archie-page-56.md',
        'archie-page-61.md',
        'archie-page-63.md',
        'archie-page-64.md'
    ]
    
    for filename in problematic_files:
        file_path = os.path.join(content_dir, filename)
        if os.path.exists(file_path):
            fix_file_yaml(file_path)

def fix_file_yaml(file_path):
    """Fix YAML issues in a specific file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split frontmatter and content
        if not content.startswith('---'):
            return
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            return
        
        frontmatter_str = parts[1].strip()
        body_content = parts[2]
        
        # Clean up the frontmatter line by line
        lines = frontmatter_str.split('\n')
        fixed_lines = []
        
        for line in lines:
            if line.strip():
                if line.startswith('title:') or line.startswith('description:'):
                    # Extract key and value
                    key, value = line.split(':', 1)
                    value = value.strip()
                    
                    # Remove any existing quotes
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    
                    # Clean the value
                    value = value.replace('"', '\\"')  # Escape internal quotes
                    value = ' '.join(value.split())  # Normalize whitespace
                    
                    # Limit description length
                    if key.strip() == 'description' and len(value) > 200:
                        value = value[:197] + "..."
                    
                    # Add back quotes
                    fixed_lines.append(f'{key}: "{value}"')
                else:
                    fixed_lines.append(line)
        
        # Reconstruct the file
        new_frontmatter = '\n'.join(fixed_lines)
        new_content = f"---\n{new_frontmatter}\n---{body_content}"
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Fixed: {os.path.basename(file_path)}")
        
    except Exception as e:
        print(f"Error fixing {file_path}: {str(e)}")

if __name__ == "__main__":
    fix_specific_yaml_issues()