#!/usr/bin/env python3
"""
replace_navbar.py

Walks every .html file in the same folder as this script (and subfolders)
and replaces one exact navbar block with another.

Usage:
    python replace_navbar.py

By default it only scans the folder the script lives in. Set RECURSIVE to
False if you only want the top-level folder (no subfolders).
"""

import os

# ---------------- CONFIG ----------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RECURSIVE = True
# -----------------------------------------

OLD_BLOCK = """<nav class="navbar navbar-dropdown navbar-expand-lg">
        <div class="container">
            <div class="navbar-brand">
                <span class="navbar-logo">
                    <a href="index.html">
                        <img src="assets/images/img-509195-1076x1068.png" alt="Mobirise Website Builder" style="height: 6.2rem;">
                    </a>
                </span>
                
            </div>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-bs-toggle="collapse" data-target="#navbarSupportedContent" data-bs-target="#navbarSupportedContent" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <div class="hamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-danger text-primary display-4" href="page4.html">DevLog</a></li>
                    
                    <li class="nav-item"><a class="nav-link link text-danger text-primary display-4" href="page5.html">Photography</a></li><li class="nav-item"><a class="nav-link link text-danger text-primary display-4" href="page26.html">Papers</a></li><li class="nav-item"><a class="nav-link link text-danger text-primary display-4" href="page31.html">Old Projects</a></li><li class="nav-item"><a class="nav-link link text-danger text-primary display-4" href="page2.html">Lawn Care</a></li></ul>
                
                
            </div>
        </div>
    </nav>"""

NEW_BLOCK = """<nav class="navbar navbar-dropdown navbar-expand-lg">
        <div class="container">
            <div class="navbar-brand">
                <span class="navbar-logo">
                    <a href="index.html">
                        <img src="assets/images/img-509195-1076x1068.png" alt="Mobirise Website Builder" style="height: 6.2rem;">
                    </a>
                </span>
                
            </div>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-bs-toggle="collapse" data-target="#navbarSupportedContent" data-bs-target="#navbarSupportedContent" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <div class="hamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-danger text-primary display-4" href="../">Home</a></li>
                    
                </ul>
                
                
            </div>
        </div>
    </nav>"""


def find_html_files(root_dir, recursive):
    if recursive:
        for dirpath, _dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.lower().endswith(".html"):
                    yield os.path.join(dirpath, filename)
    else:
        for filename in os.listdir(root_dir):
            full_path = os.path.join(root_dir, filename)
            if os.path.isfile(full_path) and filename.lower().endswith(".html"):
                yield full_path


def main():
    changed = []
    unchanged = []

    for filepath in find_html_files(SCRIPT_DIR, RECURSIVE):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if OLD_BLOCK not in content:
            unchanged.append(filepath)
            continue

        new_content = content.replace(OLD_BLOCK, NEW_BLOCK)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        changed.append(filepath)

    print(f"Updated {len(changed)} file(s):")
    for f in changed:
        print(f"  - {os.path.relpath(f, SCRIPT_DIR)}")

    if unchanged:
        print(f"\nSkipped {len(unchanged)} file(s) (navbar block not found / already different):")
        for f in unchanged:
            print(f"  - {os.path.relpath(f, SCRIPT_DIR)}")


if __name__ == "__main__":
    main()