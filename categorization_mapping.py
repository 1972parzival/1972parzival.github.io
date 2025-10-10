#!/usr/bin/env python3

# Categorization mapping for all content files
# Based on content analysis of 68 markdown files

CATEGORY_MAPPING = {
    # 3D Printing & Manufacturing
    "archie-page-52": ["3D Printing & Manufacturing", "Tools & Utilities"],  # 3D printed belt sander
    "archie-page-17": ["3D Printing & Manufacturing"],  # first 3d model
    "archie-page-66": ["3D Printing & Manufacturing"],  # 3d shoe
    "archie-page-61": ["3D Printing & Manufacturing"],  # PIP smokers box
    "archie-page-50": ["3D Printing & Manufacturing"],  # The Extruder
    "archie-page-49": ["3D Printing & Manufacturing"],  # TPU Belt
    
    # Electronics & Arduino
    "archie-page-21": ["Electronics & Arduino"],  # ultrasonic case
    "archie-page-30": ["Electronics & Arduino"],  # Basic DC motor
    "archie-page-11": ["Electronics & Arduino"],  # IR device
    "archie-page-54": ["Electronics & Arduino"],  # GPS device
    "archie-page-53": ["Electronics & Arduino"],  # GPS part 2
    "archie-page-47": ["Electronics & Arduino"],  # LoRa System
    "archie-page-7": ["Electronics & Arduino"],  # IRRC car
    "archie-page-31": ["Electronics & Arduino"],  # DC motor
    
    # Chemistry & Materials
    "archie-page-32": ["Chemistry & Materials", "Experimental"],  # Electroplating 2
    "archie-page-48": ["Chemistry & Materials", "Experimental"],  # Electroplating 3
    "archie-page-45": ["Chemistry & Materials", "Experimental"],  # Electroplating 4
    "archie-page-24": ["Chemistry & Materials"],  # basic Electrolysis
    "archie-page-35": ["Chemistry & Materials"],  # Caffeine Distillation
    "archie-page-36": ["Chemistry & Materials"],  # Ethanol Distillation
    "archie-page-37": ["Chemistry & Materials"],  # Make Sulfuric Acid
    "archie-page-57": ["Chemistry & Materials"],  # Biodegradable Plastic Part 1
    "archie-page-58": ["Chemistry & Materials"],  # Biodegradable Plastic Part 2
    "archie-page-59": ["Chemistry & Materials"],  # Biodegradable Plastic Part 3
    "archie-page-60": ["Chemistry & Materials"],  # Biodegradable Plastic Part 4
    "archie-page-63": ["Chemistry & Materials"],  # Biodegradable Plastic Part 5
    "archie-page-64": ["Chemistry & Materials"],  # Biodegradable Plastic Part 6
    "archie-page-38": ["Chemistry & Materials"],  # Soap production
    "archie-page-25": ["Chemistry & Materials"],  # Electroplating
    
    # Software & Programming
    "archie-page-41": ["Software & Programming", "Tutorial"],  # Ollama part 1: Setup
    "archie-page-42": ["Software & Programming", "Tutorial"],  # Ollama part 2: TTS
    "aii3": ["Software & Programming", "Creative & Media"],  # ASCII Art Animation
    "archie-page-9": ["Software & Programming"],  # TTS synth project
    "archie-page-5": ["Software & Programming"],  # FFMPEG
    "archie-page-43": ["Software & Programming"],  # AII3.org
    
    # Engineering & Mechanical
    "archie-page-27": ["Engineering & Mechanical", "3D Printing & Manufacturing"],  # bike bag
    "archie-page-56": ["Engineering & Mechanical", "Tools & Utilities"],  # Can Crusher
    "archie-page-65": ["Engineering & Mechanical"],  # Understanding Gears
    "archie-page-46": ["Engineering & Mechanical"],  # Two Way Air Cap
    "archie-page-44": ["Engineering & Mechanical", "Experimental"],  # DIY Pressure Containers
    "archie-page-55": ["Engineering & Mechanical"],  # DIY Refrigeration System
    
    # Academic & Documentation
    "archie-page-23": ["Academic & Documentation", "Electronics & Arduino"],  # murray state
    "archie-page-15": ["Academic & Documentation"],  # sketch notes
    "archie-page-20": ["Academic & Documentation"],  # LOGBOOK
    "archie-page-67": ["Academic & Documentation", "Research"],  # papers
    "archie-page-26": ["Academic & Documentation"],  # childhood projects
    "archie-page-29": ["Academic & Documentation"],  # Piezo
    
    # Tools & Utilities
    "archie-page-62": ["Tools & Utilities"],  # screwdriver
    "archie-page-18": ["Tools & Utilities"],  # spray assist
    "archie-page-22": ["Tools & Utilities"],  # Mini Lightbox build
    "archie-page-51": ["Tools & Utilities"],  # Board Pack
    
    # Creative & Media
    "archie-page-67": ["Creative & Media"],  # photography (if different from papers)
    "archie-page-19": ["Creative & Media"],  # DevLog
    "archie-page-39": ["Creative & Media"],  # Spray Logo
    "archie-page-40": ["Creative & Media"],  # DIY cologne/perfume
    "archie-page-28": ["Creative & Media"],  # opensauce 2024
    
    # Work & Services
    "archie-page-14": ["Work & Services"],  # lawn work
    "archie-page-16": ["Work & Services"],  # spray assist
    "archie-page-12": ["Work & Services"],  # Executive 210
    "archie-page-10": ["Work & Services"],  # Student Assist: Part 1
    "archie-page-13": ["Work & Services"],  # Student Assist: Part 2
    
    # Special pages
    "archie-home": ["Personal"],  # Archie Haddley Morris
    "archie-page-1": ["Personal"],  # Contacts
    "archie-page-2": ["Personal"],  # 404
    "archie-page-4": ["Personal"],  # Parz
    "archie-page-6": ["Personal"],  # parz.wiki
    "archie-page-8": ["Personal"],  # AquaPhyto
    "archie-page-33": ["Personal"],  # ABENICS
    "archie-page-34": ["Personal"],  # RIS
}

# Function to get categories for a file
def get_categories_for_file(filename):
    # Remove .md extension if present
    slug = filename.replace('.md', '')
    return CATEGORY_MAPPING.get(slug, ['Personal', 'Projects'])  # fallback to original

# Print the mapping for review
if __name__ == "__main__":
    print("Category Mapping Summary:")
    print("=" * 50)
    
    category_counts = {}
    for slug, categories in CATEGORY_MAPPING.items():
        for cat in categories:
            category_counts[cat] = category_counts.get(cat, 0) + 1
    
    print("\nCategory Usage:")
    for cat, count in sorted(category_counts.items()):
        print(f"{cat}: {count} files")
    
    print(f"\nTotal files mapped: {len(CATEGORY_MAPPING)}")
    print("Files not in mapping will use fallback: ['Personal', 'Projects']")