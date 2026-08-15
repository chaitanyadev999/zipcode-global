import os
import json
import re

# 1. Fix Navigation alignment
pages_dir = r'C:\Users\recla\zipcode-global\pages'
html_files = [f for f in os.listdir(pages_dir) if f.endswith('.html') and not f.startswith('shared')]
html_files.append('layout.html')

for f in html_files:
    path = os.path.join(pages_dir, f)
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    orig = content
    # Remove bad placements
    content = content.replace('<a class="nav-btn primary" href="/home/main.html">🏠 Home Page</a>', '')
    content = content.replace('<a class="nav-btn" href="/home/main.html">🏠 Home Page</a>', '')
    
    # Ensure it is the first element inside nav-links
    if '<div class="nav-links">' in content:
        content = content.replace('<div class="nav-links">', '<div class="nav-links">\n    <a class="nav-btn" href="/home/main.html">🏠 Home Page</a>', 1)
        
    if orig != content:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

# 2. Add Pincodes to search_index.json
index_path = r'C:\Users\recla\zipcode-global\home\assets\search_index.json'
with open(index_path, 'r', encoding='utf-8') as f:
    idx_data = json.load(f)

def clean_key(s):
    return re.sub(r'[^a-z0-9\s-]', '', str(s).lower()).strip().replace(' ', '-')

# Find all data JSON files
data_dirs = [
    r'C:\Users\recla\zipcode-global\scratch\pincode-dataindia',
    r'C:\Users\recla\zipcode-global\data'
]

pincode_count = 0
for d in data_dirs:
    if not os.path.exists(d): continue
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith('.json') and f != 'tree.json' and f != 'duplicates_report.json':
                try:
                    with open(os.path.join(root, f), 'r', encoding='utf-8') as jf:
                        records = json.load(jf)
                        for r in records:
                            pin = str(r.get('pincode', r.get('zip', r.get('postal_code', '')))).strip()
                            if not pin: continue
                            
                            # Determine city slug
                            city = r.get('officename', r.get('city', r.get('village', r.get('place_name', r.get('divisionname', r.get('districtname', ''))))))
                            if not city: continue
                            c_slug = clean_key(city)
                            
                            # If we have a page for this city, map the pincode to it!
                            if c_slug in idx_data['cities']:
                                idx_data['pincodes'][pin] = idx_data['cities'][c_slug]
                                pincode_count += 1
                except Exception as e:
                    print(f"Error processing {f}: {e}")

if pincode_count > 0:
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(idx_data, f, separators=(',', ':'))

print(f'Fixed nav in {len(html_files)} files. Mapped {len(idx_data["pincodes"])} pincodes!')
