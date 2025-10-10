#!/usr/bin/env python3
"""
Comprehensive spelling and grammar checker/fixer for all .md files
"""

import os
import re
import yaml
from typing import Dict, List, Tuple

def get_common_fixes() -> Dict[str, str]:
    """Common spelling and grammar fixes"""
    return {
        # Command typos we found before
        'kutectl': 'kubectl',
        'ekctl': 'kubectl', 
        'eskctl': 'kubectl',
        
        # Common spelling mistakes
        'recieve': 'receive',
        'recieved': 'received',
        'acheive': 'achieve',
        'acheived': 'achieved',
        'seperate': 'separate',
        'seperated': 'separated',
        'definately': 'definitely',
        'occured': 'occurred',
        'occurence': 'occurrence',
        'neccessary': 'necessary',
        'priviledge': 'privilege',
        'excercise': 'exercise',
        'excercising': 'exercising',
        'independant': 'independent',
        'independantly': 'independently',
        'existance': 'existence',
        'experiance': 'experience',
        'experiances': 'experiences',
        'experinced': 'experienced',
        'performace': 'performance',
        'enviroment': 'environment',
        'enviroments': 'environments',
        'intresting': 'interesting',
        'begining': 'beginning',
        'sucessful': 'successful',
        'sucessfully': 'successfully',
        'sucess': 'success',
        'writting': 'writing',
        'writtten': 'written',
        'lenght': 'length',
        'widht': 'width',
        'hieght': 'height',
        'strenght': 'strength',
        'treshold': 'threshold',
        'thier': 'their',
        'wich': 'which',
        'witch': 'which',  # when used as conjunction
        'untill': 'until',
        'allready': 'already',
        'alot': 'a lot',
        'its self': 'itself',
        'it self': 'itself',
        'my self': 'myself',
        'your self': 'yourself',
        'him self': 'himself',
        'her self': 'herself',
        
        # Technical terms
        'Javascript': 'JavaScript',
        'javascript': 'JavaScript',
        'Github': 'GitHub',
        'github': 'GitHub',
        'Nodejs': 'Node.js',
        'nodejs': 'Node.js',
        'Postgresql': 'PostgreSQL',
        'postgresql': 'PostgreSQL',
        'Mysql': 'MySQL',
        'mysql': 'MySQL',
        'Api': 'API',
        'Apis': 'APIs',
        'Url': 'URL',
        'Urls': 'URLs',
        'Html': 'HTML',
        'Css': 'CSS',
        'Json': 'JSON',
        'Xml': 'XML',
        'Yaml': 'YAML',
        'Sql': 'SQL',
        'Csv': 'CSV',
        'Pdf': 'PDF',
        'Ide': 'IDE',
        'Cli': 'CLI',
        'Gui': 'GUI',
        'Sdk': 'SDK',
        'Tcp': 'TCP',
        'Udp': 'UDP',
        'Http': 'HTTP',
        'Https': 'HTTPS',
        'Ftp': 'FTP',
        'Ssh': 'SSH',
        'Ssl': 'SSL',
        'Tls': 'TLS',
        
        # Grammar fixes
        'also offer': 'also offers',
        'also provide': 'also provides',
        'also include': 'also includes',
        'also contain': 'also contains',
        'also support': 'also supports',
        'also allow': 'also allows',
        'also enable': 'also enables',
        'also help': 'also helps',
        'also give': 'also gives',
        'also show': 'also shows',
        'also make': 'also makes',
        'also take': 'also takes',
        'also use': 'also uses',
        'also work': 'also works',
        'also run': 'also runs',
        'also create': 'also creates',
        'also build': 'also builds',
        'also generate': 'also generates',
        'also handle': 'also handles',
        'also manage': 'also manages',
        'also process': 'also processes',
        
        # Double spaces and formatting
        '  ': ' ',  # Double spaces to single
    }

def get_word_boundary_fixes() -> Dict[str, str]:
    """Fixes that should only be applied at word boundaries"""
    return {
        'thru': 'through',
        'tho': 'though',
        'ur': 'your',
        'u': 'you',  # Only in informal contexts
        'dont': "don't",
        'doesnt': "doesn't",
        'cant': "can't",
        'wont': "won't",
        'isnt': "isn't",
        'arent': "aren't",
        'wasnt': "wasn't",
        'werent': "weren't",
        'hasnt': "hasn't",
        'havent': "haven't",
        'hadnt': "hadn't",
        'shouldnt': "shouldn't",
        'wouldnt': "wouldn't",
        'couldnt': "couldn't",
        'mustnt': "mustn't",
        'neednt': "needn't",
        'oughtnt': "oughtn't",
    }

def apply_fixes(content: str, fixes: Dict[str, str], use_word_boundary: bool = False) -> Tuple[str, List[str]]:
    """Apply fixes to content and return fixed content and list of changes made"""
    changes = []
    
    for wrong, correct in fixes.items():
        if use_word_boundary:
            # Use word boundary regex for more precise matching
            pattern = r'\b' + re.escape(wrong) + r'\b'
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                content = re.sub(pattern, correct, content, flags=re.IGNORECASE)
                changes.extend([f"'{match}' -> '{correct}'" for match in matches])
        else:
            # Simple string replacement
            if wrong in content:
                count = content.count(wrong)
                content = content.replace(wrong, correct)
                changes.extend([f"'{wrong}' -> '{correct}'" for _ in range(count)])
    
    return content, changes

def fix_markdown_file(filepath: str) -> List[str]:
    """Fix spelling and grammar in a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        content = original_content
        all_changes = []
        
        # Apply regular fixes
        content, changes1 = apply_fixes(content, get_common_fixes())
        all_changes.extend(changes1)
        
        # Apply word boundary fixes
        content, changes2 = apply_fixes(content, get_word_boundary_fixes(), use_word_boundary=True)
        all_changes.extend(changes2)
        
        # Fix multiple consecutive spaces (but preserve code blocks)
        lines = content.split('\n')
        fixed_lines = []
        in_code_block = False
        
        for line in lines:
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
            
            if not in_code_block:
                # Fix multiple spaces outside code blocks
                original_line = line
                line = re.sub(r' +', ' ', line)  # Multiple spaces to single
                line = line.strip() + '\n' if line.strip() else line  # Remove trailing spaces
                if original_line != line and original_line.strip():
                    all_changes.append(f"Fixed spacing in line: '{original_line.strip()}'")
            
            fixed_lines.append(line)
        
        content = '\n'.join(fixed_lines)
        
        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return all_changes
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return []

def main():
    # Get all .md files
    content_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/content"
    root_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io"
    
    md_files = []
    
    # Get .md files from content directory
    if os.path.exists(content_dir):
        for filename in os.listdir(content_dir):
            if filename.endswith('.md'):
                md_files.append(os.path.join(content_dir, filename))
    
    # Get .md files from root directory
    for filename in os.listdir(root_dir):
        if filename.endswith('.md'):
            md_files.append(os.path.join(root_dir, filename))
    
    # Also check subdirectories for .md files
    for root, dirs, files in os.walk(root_dir):
        # Skip node_modules, .git, .next, etc.
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '_next', 'out', 'dist', '__pycache__']]
        
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                if filepath not in md_files:
                    md_files.append(filepath)
    
    print(f"Found {len(md_files)} .md files to check")
    
    total_changes = 0
    files_changed = 0
    
    for filepath in sorted(md_files):
        relative_path = os.path.relpath(filepath, root_dir)
        changes = fix_markdown_file(filepath)
        
        if changes:
            files_changed += 1
            total_changes += len(changes)
            print(f"\n✅ {relative_path} - {len(changes)} fixes:")
            for change in changes[:10]:  # Show first 10 changes
                print(f"   • {change}")
            if len(changes) > 10:
                print(f"   ... and {len(changes) - 10} more changes")
        else:
            print(f"✓ {relative_path} - No issues found")
    
    print(f"\n📊 Summary:")
    print(f"   • Files processed: {len(md_files)}")
    print(f"   • Files changed: {files_changed}")
    print(f"   • Total fixes applied: {total_changes}")

if __name__ == "__main__":
    main()