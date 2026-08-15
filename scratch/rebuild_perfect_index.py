import os
import json
import re

base_dir = r'C:\Users\recla\zipcode-global'
pages_dir = os.path.join(base_dir, 'pages')
index_path = os.path.join(base_dir, 'home', 'assets', 'search_index.json')

index = {
    'countries': {},
    'states': {},
    'cities': {},
    'pincodes': {}
}

def clean_key(s):
    return re.sub(r'[^a-z0-9\s-]', '', str(s).lower()).strip().replace(' ', '-')

print("Indexing Countries, States, and Cities based on existing HTML files...")

# Scan pages directory
for item in os.listdir(pages_dir):
    item_path = os.path.join(pages_dir, item)
    
    # Countries: pages/*.html
    if os.path.isfile(item_path) and item.endswith('.html') and not item.startswith('shared') and item != 'layout.html' and item != 'translate.html' and item != 'blog.html' and item != 'about.html' and item != 'privacy.html' and item != 'report.html':
        country_slug = item.replace('.html', '')
        index['countries'][country_slug] = f'pages/{item}'
        
    # Explore country directories for states and cities
    if os.path.isdir(item_path):
        country_slug = item
        
        for sub_item in os.listdir(item_path):
            sub_item_path = os.path.join(item_path, sub_item)
            
            # States: pages/country/*.html
            if os.path.isfile(sub_item_path) and sub_item.endswith('.html'):
                state_slug = sub_item.replace('.html', '')
                index['states'][state_slug] = f'pages/{country_slug}/{sub_item}'
                
            # Cities: pages/country/state/*.html
            if os.path.isdir(sub_item_path):
                state_slug = sub_item
                for city_item in os.listdir(sub_item_path):
                    if city_item.endswith('.html'):
                        city_slug = city_item.replace('.html', '')
                        # Skip if it's an accidental state file inside the state folder
                        if city_slug == state_slug: continue
                        index['cities'][city_slug] = f'pages/{country_slug}/{state_slug}/{city_item}'

print(f"Indexed {len(index['countries'])} countries, {len(index['states'])} states, and {len(index['cities'])} cities.")

print("Extracting Pincodes from all local JSON data...")
pincode_count = 0
for root, dirs, files in os.walk(base_dir):
    if '.git' in root or 'node_modules' in root or 'home\\assets' in root:
        continue
    for f in files:
        if f.endswith('.json') and f != 'tree.json' and f != 'duplicates_report.json' and f != 'search_index.json':
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as jf:
                    records = json.load(jf)
                    if isinstance(records, dict):
                        for key in records:
                            if isinstance(records[key], list):
                                records = records[key]
                                break
                    if isinstance(records, list):
                        for r in records:
                            if not isinstance(r, dict): continue
                            pin = str(r.get('pincode', r.get('zip', r.get('postal_code', '')))).strip()
                            if not pin: continue
                            
                            city = r.get('officename', r.get('city', r.get('village', r.get('place_name', r.get('divisionname', r.get('districtname', ''))))))
                            if not city: continue
                            
                            c_slug = clean_key(city)
                            if c_slug in index['cities']:
                                index['pincodes'][pin] = index['cities'][c_slug]
                                pincode_count += 1
            except Exception as e:
                pass

print(f"Mapped {pincode_count} pincodes to existing cities.")

# Save the unified index
with open(index_path, 'w', encoding='utf-8') as f:
    json.dump(index, f, separators=(',', ':'))

print("search_index.json has been perfectly rebuilt!")
