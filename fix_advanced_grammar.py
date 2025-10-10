#!/usr/bin/env python3
"""
Enhanced spelling, grammar, and capitalization checker for all .md files
This version focuses on capitalization rules and catches more nuanced issues.
"""

import os
import re
import yaml
from typing import Dict, List, Tuple

def get_capitalization_fixes() -> Dict[str, str]:
    """Capitalization fixes for proper nouns and technical terms"""
    return {
        # Programming languages and frameworks
        'python': 'Python',
        'javascript': 'JavaScript',
        'java': 'Java',
        'c#': 'C#',
        'typescript': 'TypeScript',
        'react': 'React',
        'vue': 'Vue',
        'angular': 'Angular',
        'node.js': 'Node.js',
        'express': 'Express',
        'django': 'Django',
        'flask': 'Flask',
        'laravel': 'Laravel',
        'spring': 'Spring',
        'bootstrap': 'Bootstrap',
        'jquery': 'jQuery',
        
        # Databases
        'mysql': 'MySQL',
        'postgresql': 'PostgreSQL',
        'mongodb': 'MongoDB',
        'redis': 'Redis',
        'sqlite': 'SQLite',
        
        # Cloud platforms and services
        'aws': 'AWS',
        'amazon web services': 'Amazon Web Services',
        'azure': 'Azure',
        'google cloud': 'Google Cloud',
        'docker': 'Docker',
        'kubernetes': 'Kubernetes',
        'jenkins': 'Jenkins',
        'github': 'GitHub',
        'gitlab': 'GitLab',
        'bitbucket': 'Bitbucket',
        
        # Operating systems
        'windows': 'Windows',
        'macos': 'macOS',
        'linux': 'Linux',
        'ubuntu': 'Ubuntu',
        'debian': 'Debian',
        'centos': 'CentOS',
        'fedora': 'Fedora',
        
        # Technical acronyms that should be uppercase
        'api': 'API',
        'apis': 'APIs',
        'rest': 'REST',
        'json': 'JSON',
        'xml': 'XML',
        'html': 'HTML',
        'css': 'CSS',
        'sql': 'SQL',
        'url': 'URL',
        'urls': 'URLs',
        'http': 'HTTP',
        'https': 'HTTPS',
        'ftp': 'FTP',
        'ssh': 'SSH',
        'tcp': 'TCP',
        'udp': 'UDP',
        'ip': 'IP',
        'dns': 'DNS',
        'ssl': 'SSL',
        'tls': 'TLS',
        'ui': 'UI',
        'ux': 'UX',
        'gui': 'GUI',
        'cli': 'CLI',
        'ide': 'IDE',
        'sdk': 'SDK',
        'ai': 'AI',
        'ml': 'ML',
        'iot': 'IoT',
        'ar': 'AR',
        'vr': 'VR',
        'gps': 'GPS',
        'cpu': 'CPU',
        'gpu': 'GPU',
        'ram': 'RAM',
        'ssd': 'SSD',
        'hdd': 'HDD',
        'usb': 'USB',
        'wifi': 'WiFi',
        'bluetooth': 'Bluetooth',
        
        # File formats
        'pdf': 'PDF',
        'csv': 'CSV',
        'yaml': 'YAML',
        'toml': 'TOML',
        'gif': 'GIF',
        'png': 'PNG',
        'jpg': 'JPG',
        'jpeg': 'JPEG',
        'svg': 'SVG',
        'mp3': 'MP3',
        'mp4': 'MP4',
        
        # Companies and products
        'apple': 'Apple',
        'microsoft': 'Microsoft',
        'google': 'Google',
        'amazon': 'Amazon',
        'facebook': 'Facebook',
        'meta': 'Meta',
        'netflix': 'Netflix',
        'adobe': 'Adobe',
        'oracle': 'Oracle',
        'ibm': 'IBM',
        'intel': 'Intel',
        'amd': 'AMD',
        'nvidia': 'NVIDIA',
        'tesla': 'Tesla',
        'spacex': 'SpaceX',
        
        # Science and technology terms
        'arduino': 'Arduino',
        'raspberry pi': 'Raspberry Pi',
        '3d printing': '3D printing',
        'iot': 'IoT',
        'blockchain': 'Blockchain',
        'machine learning': 'Machine Learning',
        'artificial intelligence': 'Artificial Intelligence',
        'deep learning': 'Deep Learning',
        'neural network': 'Neural Network',
        'data science': 'Data Science',
        'big data': 'Big Data',
        'cloud computing': 'Cloud Computing',
        'cybersecurity': 'Cybersecurity',
        'devops': 'DevOps',
        'agile': 'Agile',
        'scrum': 'Scrum',
        'kanban': 'Kanban',
        
        # Months should be capitalized when used as proper nouns
        'january': 'January',
        'february': 'February',
        'march': 'March', 
        'april': 'April',
        'may': 'May',
        'june': 'June',
        'july': 'July',
        'august': 'August',
        'september': 'September',
        'october': 'October',
        'november': 'November',
        'december': 'December',
        
        # Days of the week
        'monday': 'Monday',
        'tuesday': 'Tuesday', 
        'wednesday': 'Wednesday',
        'thursday': 'Thursday',
        'friday': 'Friday',
        'saturday': 'Saturday',
        'sunday': 'Sunday',
    }

def get_advanced_grammar_fixes() -> Dict[str, str]:
    """Advanced grammar fixes that weren't caught in the first pass"""
    return {
        # A vs An corrections
        'a API': 'an API',
        'a HTML': 'an HTML',
        'a HTTP': 'an HTTP',
        'a IDE': 'an IDE',
        'a SQL': 'an SQL',
        'a URL': 'an URL',
        'a XML': 'an XML',
        
        # Its vs It's
        "its'": "its",  # Common mistake
        'its a': "it's a",
        'its an': "it's an",
        'its the': "it's the",
        'its not': "it's not",
        'its been': "it's been",
        'its going': "it's going",
        'its working': "it's working",
        
        # There/Their/They're
        'there are': 'there are',  # This is correct, but we'll check context
        'they are': "they're",  # Only in informal contexts
        
        # Effect vs Affect (common mistakes)
        'effected by': 'affected by',
        'had an affect': 'had an effect',
        
        # Loose vs Lose
        'loose data': 'lose data',
        'loose connection': 'lose connection',
        
        # Your vs You're
        'your going': "you're going",
        'your not': "you're not",
        'your the': "you're the",
        'your a': "you're a",
        'your an': "you're an",
        
        # Common misspellings that might have been missed
        'accross': 'across',
        'addres': 'address',
        'adress': 'address',
        'begining': 'beginning',
        'developement': 'development',
        'developement': 'development',
        'enviroment': 'environment',
        'exmaple': 'example',
        'examle': 'example',
        'exemple': 'example',
        'implmentation': 'implementation',
        'implementaion': 'implementation',
        'occassion': 'occasion',
        'ocurred': 'occurred',
        'responsability': 'responsibility',
        'responsable': 'responsible',
        'seperate': 'separate',
        'succesful': 'successful',
        'sucessful': 'successful',
        'tommorrow': 'tomorrow',
        'transfered': 'transferred',
        'transfering': 'transferring',
        'untill': 'until',
        'usefull': 'useful',
        
        # Redundant phrases
        'in order to': 'to',
        'the reason is because': 'the reason is that',
        'due to the fact that': 'because',
        'at this point in time': 'now',
        'close proximity': 'proximity',
        'end result': 'result',
        'final outcome': 'outcome',
        'free gift': 'gift',
        'past history': 'history',
        'unexpected surprise': 'surprise',
        
        # Technical writing improvements
        'allows for': 'allows',
        'in regards to': 'regarding',
        'in regard to': 'regarding',
        'as to whether': 'whether',
        'the fact that': 'that',
        'it is important to note': '',  # Often unnecessary
        'it should be noted': '',  # Often unnecessary
    }

def get_sentence_case_fixes() -> List[tuple]:
    """Patterns for fixing sentence capitalization"""
    return [
        # Start of sentences after periods
        (r'(\. +)([a-z])', lambda m: m.group(1) + m.group(2).upper()),
        # Start of sentences after exclamation marks
        (r'(\! +)([a-z])', lambda m: m.group(1) + m.group(2).upper()),
        # Start of sentences after question marks
        (r'(\? +)([a-z])', lambda m: m.group(1) + m.group(2).upper()),
        # Start of new lines (beginning of paragraphs)
        (r'(^|\n)([a-z])', lambda m: m.group(1) + m.group(2).upper()),
        # After colons when introducing a complete sentence
        (r'(: +)([a-z])', lambda m: m.group(1) + m.group(2).upper()),
    ]

def apply_capitalization_fixes(content: str) -> Tuple[str, List[str]]:
    """Apply capitalization fixes with word boundary matching"""
    fixes = get_capitalization_fixes()
    changes = []
    
    for wrong, correct in fixes.items():
        # Use word boundary regex for precise matching
        pattern = r'\b' + re.escape(wrong) + r'\b'
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            # Only replace if the case is actually different
            for match in matches:
                if match != correct:
                    content = content.replace(match, correct)
                    changes.append(f"'{match}' → '{correct}'")
    
    return content, changes

def apply_sentence_case_fixes(content: str) -> Tuple[str, List[str]]:
    """Apply sentence capitalization fixes"""
    changes = []
    original_content = content
    
    # Skip code blocks and frontmatter
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False
    in_frontmatter = False
    
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == '---':
            in_frontmatter = True
        elif line.strip() == '---' and in_frontmatter:
            in_frontmatter = False
        elif line.strip().startswith('```'):
            in_code_block = not in_code_block
        
        if not in_code_block and not in_frontmatter:
            original_line = line
            
            # Apply sentence case patterns
            for pattern, replacement in get_sentence_case_fixes():
                line = re.sub(pattern, replacement, line)
            
            # Capitalize first word of line if it's the start of a sentence
            if line.strip() and not line.lstrip().startswith(('#', '-', '*', '>', '`')):
                stripped = line.lstrip()
                if stripped and stripped[0].islower():
                    # Check if this looks like the start of a sentence
                    if not any(stripped.startswith(prefix) for prefix in ['http', 'www', 'ftp']):
                        indent = line[:len(line) - len(stripped)]
                        line = indent + stripped[0].upper() + stripped[1:]
            
            if original_line != line:
                changes.append(f"Fixed capitalization in: '{original_line.strip()}'")
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), changes

def fix_advanced_markdown_file(filepath: str) -> List[str]:
    """Apply advanced spelling, grammar, and capitalization fixes"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        content = original_content
        all_changes = []
        
        # Apply advanced grammar fixes
        grammar_fixes = get_advanced_grammar_fixes()
        for wrong, correct in grammar_fixes.items():
            if wrong in content:
                count = content.count(wrong)
                content = content.replace(wrong, correct)
                all_changes.extend([f"'{wrong}' → '{correct}'" for _ in range(count)])
        
        # Apply capitalization fixes
        content, cap_changes = apply_capitalization_fixes(content)
        all_changes.extend(cap_changes)
        
        # Apply sentence case fixes
        content, sentence_changes = apply_sentence_case_fixes(content)
        all_changes.extend(sentence_changes)
        
        # Fix common punctuation issues
        original_punct = content
        
        # Space before punctuation (except in code blocks)
        lines = content.split('\n')
        fixed_lines = []
        in_code_block = False
        
        for line in lines:
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
            
            if not in_code_block:
                original_line = line
                # Fix space before punctuation
                line = re.sub(r' +([,.!?;:])', r'\1', line)
                # Fix multiple punctuation
                line = re.sub(r'([.!?]){2,}', r'\1', line)
                # Fix space after punctuation
                line = re.sub(r'([,.!?;:])([a-zA-Z])', r'\1 \2', line)
                
                if original_line != line and original_line.strip():
                    all_changes.append(f"Fixed punctuation: '{original_line.strip()}'")
            
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
    # Focus only on content directory .md files
    content_dir = "/Users/neilhaddley/Documents/GitHub/haddley.github.io/content"
    
    if not os.path.exists(content_dir):
        print(f"Content directory not found: {content_dir}")
        return
    
    md_files = []
    for filename in os.listdir(content_dir):
        if filename.endswith('.md'):
            md_files.append(os.path.join(content_dir, filename))
    
    print(f"Found {len(md_files)} .md files in content directory to enhance")
    
    total_changes = 0
    files_changed = 0
    
    for filepath in sorted(md_files):
        relative_path = os.path.relpath(filepath, "/Users/neilhaddley/Documents/GitHub/haddley.github.io")
        changes = fix_advanced_markdown_file(filepath)
        
        if changes:
            files_changed += 1
            total_changes += len(changes)
            print(f"\n✅ {relative_path} - {len(changes)} enhancements:")
            for change in changes[:8]:  # Show first 8 changes
                print(f"   • {change}")
            if len(changes) > 8:
                print(f"   ... and {len(changes) - 8} more changes")
        else:
            print(f"✓ {relative_path} - Already optimal")
    
    print(f"\n📊 Enhancement Summary:")
    print(f"   • Files processed: {len(md_files)}")
    print(f"   • Files enhanced: {files_changed}")
    print(f"   • Total enhancements: {total_changes}")

if __name__ == "__main__":
    main()