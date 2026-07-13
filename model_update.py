#!/usr/bin/env python3
"""
add_blog_posts.py

Scans a folder of blog .html files and adds any posts missing from
models.json, using sensible defaults.

Defaults for new entries:
    name -> derived from the html filename (e.g. "my-cool-post.html" -> "My Cool Post")
    file -> "logo.obj"
    site -> "./blog/<filename>.html"

Existing entries are left untouched. A post is considered "already added"
if its site path already appears in models.json.

Usage:
    python add_blog_posts.py

Adjust the CONFIG section below to match your project layout.
"""

import json
import os
import re

# ---------------- CONFIG ----------------
MODELS_JSON_PATH = os.path.join("public", "models.json")
BLOG_DIR = os.path.join("public", "blog")
DEFAULT_FILE = "logo.obj"
# -----------------------------------------


def filename_to_name(filename: str) -> str:
    """Turn 'my-cool-post.html' into 'My Cool Post'."""
    stem = os.path.splitext(filename)[0]
    words = stem.replace("_", "-").split("-")
    return " ".join(w.capitalize() for w in words if w)


def sort_key(filename: str):
    """Sort by leading number in filename if present, else alphabetically.

    e.g. '2-gps-system.html' -> (0, 2, ...)
         '10-mini-lightbox.html' -> (0, 10, ...)
         'about-us.html' -> (1, 0, 'about-us.html')
    """
    match = re.match(r"^(\d+)", filename)
    if match:
        return (0, int(match.group(1)), filename.lower())
    return (1, 0, filename.lower())


def load_models(path: str):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            return []
        return json.loads(content)


def save_models(path: str, models: list):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(models, f, indent=4)
        f.write("\n")


def main():
    if not os.path.isdir(BLOG_DIR):
        print(f"Blog directory not found: {BLOG_DIR}")
        return

    models = load_models(MODELS_JSON_PATH)
    existing_sites = {entry.get("site") for entry in models}

    html_files = sorted(
        (f for f in os.listdir(BLOG_DIR) if f.lower().endswith(".html")),
        key=sort_key,
    )

    added = []
    for filename in html_files:
        site = f"./blog/{filename}"
        if site in existing_sites:
            continue

        entry = {
            "name": filename_to_name(filename),
            "file": DEFAULT_FILE,
            "site": site,
        }
        models.append(entry)
        added.append(entry)

    if added:
        save_models(MODELS_JSON_PATH, models)
        print(f"Added {len(added)} new post(s) to {MODELS_JSON_PATH}:")
        for entry in added:
            print(f"  - {entry['name']} ({entry['site']})")
    else:
        print("No new posts found. models.json is already up to date.")


if __name__ == "__main__":
    main()