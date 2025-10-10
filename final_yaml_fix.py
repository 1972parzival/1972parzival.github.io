#!/usr/bin/env python3

import os
import re
from pathlib import Path

def fix_specific_yaml_issues(file_path):
    """Fix specific YAML frontmatter issues that are causing build errors"""
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
        
        # Fix 1: Remove spaces from image filenames with extensions
        # e.g., "image-3. PNG" -> "image-3.PNG"
        def fix_spaced_extensions(text):
            # Match patterns like ". JPG", ". PNG", ". JPEG" etc.
            pattern = r'(\w+)\.\s+(jpg|jpeg|png|gif|webp|svg|JPG|JPEG|PNG|GIF|WEBP|SVG)'
            def replacer(match):
                filename = match.group(1)
                ext = match.group(2)
                return f"{filename}.{ext}"
            return re.sub(pattern, replacer, text)
        
        frontmatter = fix_spaced_extensions(frontmatter)
        if frontmatter != original_frontmatter:
            fixes_made.append("Fixed spaced file extensions")
            original_frontmatter = frontmatter
        
        # Fix 2: Quote all image paths properly
        image_pattern = r'^(\s*image:\s*)([^"\n].*)$'
        def quote_all_images(match):
            prefix = match.group(1)
            path = match.group(2).strip()
            if not (path.startswith('"') and path.endswith('"')):
                return f'{prefix}"{path}"'
            return match.group(0)
        
        frontmatter = re.sub(image_pattern, quote_all_images, frontmatter, flags=re.MULTILINE)
        if frontmatter != original_frontmatter:
            fixes_made.append("Quoted image paths")
            original_frontmatter = frontmatter
        
        # Fix 3: Fix truncated descriptions with unmatched quotes
        desc_pattern = r'^(\s*description:\s*"[^"]*)"?\s*$'
        def fix_descriptions(match):
            desc_line = match.group(0)
            if not desc_line.rstrip().endswith('"'):
                return desc_line.rstrip() + '"'
            return desc_line
        
        frontmatter = re.sub(desc_pattern, fix_descriptions, frontmatter, flags=re.MULTILINE)
        if frontmatter != original_frontmatter:
            fixes_made.append("Fixed description quotes")
            original_frontmatter = frontmatter
        
        # Fix 4: Fix problematic characters in descriptions
        # Replace patterns like "Vi." with "Video" or quote them properly
        if 'Vi.' in frontmatter:
            frontmatter = frontmatter.replace('Vi.', 'Video')
            fixes_made.append("Fixed Vi. pattern")
        
        # Fix 5: Fix colon-heavy descriptions that might break YAML
        # Look for descriptions with multiple colons
        desc_with_colons_pattern = r'(description:\s*"[^"]*:[^"]*:[^"]*")([^"])'
        if re.search(desc_with_colons_pattern, frontmatter):
            # For complex descriptions with multiple colons, use block scalar
            def fix_complex_desc(match):
                desc_content = match.group(1)
                # Extract the description text
                desc_text = re.search(r'description:\s*"([^"]*)"', desc_content)
                if desc_text:
                    text = desc_text.group(1)
                    return f'description: |\n  {text}'
                return desc_content
            
            frontmatter = re.sub(desc_with_colons_pattern, fix_complex_desc, frontmatter)
            fixes_made.append("Fixed complex descriptions with colons")
        
        # Fix 6: Ensure dates are not quoted (YAML accepts ISO dates without quotes)
        date_pattern = r'^(\s*date:\s*)"([^"]+)"(\s*)$'
        frontmatter = re.sub(date_pattern, r'\1\2\3', frontmatter, flags=re.MULTILINE)
        if frontmatter != original_frontmatter:
            fixes_made.append("Unquoted dates")
            original_frontmatter = frontmatter
        
        # Fix 7: Clean up any remaining formatting issues
        lines = frontmatter.split('\n')
        cleaned_lines = []
        for line in lines:
            line = line.rstrip()  # Remove trailing spaces
            if line:  # Skip empty lines
                cleaned_lines.append(line)
        
        frontmatter = '\n'.join(cleaned_lines)
        
        # Write back the fixed content if changes were made
        if frontmatter != original_frontmatter or fixes_made:
            if not fixes_made:
                fixes_made.append("General cleanup")
            
            new_content = f"---\n{frontmatter}\n---{body}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, f"Fixed: {', '.join(fixes_made)}"
        
        return False, "No fixes needed"
        
    except Exception as e:
        return False, f"Error processing file: {str(e)}"

def main():
    """Fix specific YAML frontmatter issues causing build errors"""
    content_dir = Path("content")
    
    if not content_dir.exists():
        print("Content directory not found!")
        return
    
    total_files = 0
    fixed_files = 0
    
    print("🔧 Fixing specific YAML frontmatter issues...")
    print("=" * 50)
    
    # Process all .md files
    for md_file in content_dir.rglob("*.md"):
        total_files += 1
        success, message = fix_specific_yaml_issues(md_file)
        
        if success:
            fixed_files += 1
            print(f"✅ {md_file.name}: {message}")
        elif "No frontmatter" not in message and "No fixes needed" not in message:
            print(f"❌ {md_file.name}: {message}")
    
    print("\n" + "=" * 50)
    print(f"📊 Summary:")
    print(f"   Total files processed: {total_files}")
    print(f"   Files fixed: {fixed_files}")
    print(f"   Files with no issues: {total_files - fixed_files}")

if __name__ == "__main__":
    main()