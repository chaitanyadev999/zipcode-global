import os
import json

base_dir = r"C:\Users\recla\zipcode-global\pages\blog"
files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

missing_covers = []
missing_style = []

for f in files:
    with open(os.path.join(base_dir, f), 'r', encoding='utf-8') as file:
        txt = file.read()
        if 'class="cover"' not in txt:
            missing_covers.append(f)
        if '<style>' not in txt and '<link ' not in txt:
            missing_style.append(f)

print("Missing covers:", missing_covers)
print("Missing style:", missing_style)
