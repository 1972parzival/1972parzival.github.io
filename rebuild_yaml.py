#!/usr/bin/env python3

import os
import re
from pathlib import Path

def completely_rebuild_yaml_frontmatter(file_path):
    """Completely rebuild YAML frontmatter to ensure proper structure"""
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
        
        # Extract values from the existing frontmatter
        extracted_data = {}
        
        # Extract categories
        categories_match = re.search(r'categories:\s*\[(.*?)\]', frontmatter)
        if categories_match:
            categories_str = categories_match.group(1)
            # Split and clean up categories
            categories = [cat.strip().strip('"\'') for cat in categories_str.split(',') if cat.strip()]
            extracted_data['categories'] = categories
        else:
            # Try to extract from multi-line format
            categories_matches = re.findall(r'-\s*([^\n]+)', frontmatter)
            if categories_matches:
                extracted_data['categories'] = [cat.strip().strip('"\'') for cat in categories_matches]
            else:
                extracted_data['categories'] = ['Personal', 'Projects']
        
        # Extract date
        date_match = re.search(r'date:\s*["\']?([^"\'\n]+)["\']?', frontmatter)
        if date_match:
            extracted_data['date'] = date_match.group(1).strip()
        else:
            extracted_data['date'] = '2025-10-06'
        
        # Extract description
        desc_match = re.search(r'description:\s*["\']([^"\']*)["\']?', frontmatter)
        if desc_match:
            extracted_data['description'] = desc_match.group(1).strip()
        else:
            # Try to extract from multiline
            desc_lines = []
            in_description = False
            for line in frontmatter.split('\n'):
                if line.strip().startswith('description:'):
                    desc_text = line.split('description:', 1)[1].strip().strip('"\'')
                    if desc_text:
                        desc_lines.append(desc_text)
                    in_description = True
                elif in_description and line.strip() and not ':' in line:
                    desc_lines.append(line.strip().strip('"\''))
                elif in_description and ':' in line:
                    break
            
            if desc_lines:
                extracted_data['description'] = ' '.join(desc_lines)
            else:
                extracted_data['description'] = 'A project showcase and documentation.'
        
        # Extract image
        image_match = re.search(r'image:\s*["\']?([^"\'\n]+)["\']?', frontmatter)
        if image_match:
            image_path = image_match.group(1).strip()
            # Clean up the image path
            image_path = re.sub(r'\s+', '', image_path)  # Remove any spaces
            extracted_data['image'] = image_path
        else:
            extracted_data['image'] = '/assets/images/default.jpg'
        
        # Extract slug
        slug_match = re.search(r'slug:\s*([^\n]+)', frontmatter)
        if slug_match:
            extracted_data['slug'] = slug_match.group(1).strip()
        else:
            extracted_data['slug'] = file_path.stem
        
        # Extract title
        title_match = re.search(r'title:\s*([^\n]+)', frontmatter)
        if title_match:
            extracted_data['title'] = title_match.group(1).strip()
        else:
            extracted_data['title'] = file_path.stem.replace('-', ' ').title()
        
        # Extract tags
        tags_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter)
        if tags_match:
            tags_str = tags_match.group(1)
            if tags_str.strip():
                tags = [tag.strip().strip('"\'') for tag in tags_str.split(',') if tag.strip()]
                extracted_data['tags'] = tags
            else:
                extracted_data['tags'] = []
        else:
            extracted_data['tags'] = []
        
        # Build new clean YAML frontmatter
        new_frontmatter_lines = []
        
        # Categories
        if len(extracted_data['categories']) == 1:
            new_frontmatter_lines.append(f"categories: [{extracted_data['categories'][0]}]")
        else:
            categories_str = ', '.join(extracted_data['categories'])
            new_frontmatter_lines.append(f"categories: [{categories_str}]")
        
        # Date
        new_frontmatter_lines.append(f"date: '{extracted_data['date']}'")
        
        # Description
        clean_desc = extracted_data['description'].replace('"', '\\"')
        new_frontmatter_lines.append(f'description: "{clean_desc}"')
        
        # Image
        new_frontmatter_lines.append(f'image: "{extracted_data["image"]}"')
        
        # Slug
        new_frontmatter_lines.append(f"slug: {extracted_data['slug']}")
        
        # Tags
        if extracted_data['tags']:
            tags_str = ', '.join(extracted_data['tags'])
            new_frontmatter_lines.append(f"tags: [{tags_str}]")
        else:
            new_frontmatter_lines.append("tags: []")
        
        # Title
        new_frontmatter_lines.append(f"title: {extracted_data['title']}")
        
        new_frontmatter = '\n'.join(new_frontmatter_lines)
        
        # Write back the completely rebuilt content
        new_content = f"---\n{new_frontmatter}\n---{body}"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Completely rebuilt YAML frontmatter"
        
    except Exception as e:
        return False, f"Error processing file: {str(e)}"

def main():
    """Completely rebuild YAML frontmatter for all markdown files"""
    content_dir = Path("content")
    
    if not content_dir.exists():
        print("Content directory not found!")
        return
    
    total_files = 0
    fixed_files = 0
    
    print("🔧 Completely rebuilding YAML frontmatter for all files...")
    print("=" * 60)
    
    # Process all .md files
    for md_file in content_dir.rglob("*.md"):
        total_files += 1
        success, message = completely_rebuild_yaml_frontmatter(md_file)
        
        if success:
            fixed_files += 1
            print(f"✅ {md_file.name}: {message}")
        else:
            print(f"❌ {md_file.name}: {message}")
    
    print("\n" + "=" * 60)
    print(f"📊 Summary:")
    print(f"   Total files processed: {total_files}")
    print(f"   Files rebuilt: {fixed_files}")
    print(f"   Success rate: {(fixed_files/total_files)*100:.1f}%")

if __name__ == "__main__":
    main()