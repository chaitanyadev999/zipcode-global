import os
import json

data_repo = r"C:\Users\recla\zipcode-global\scratch\pincode-dataindia"
output_file = r"C:\Users\recla\zipcode-global\home\assets\search_index.json"

index = {
    "countries": {},
    "states": {},
    "cities": {},
    "pincodes": {}
}

# Add countries
index["countries"]["india"] = "pages/india.html"
index["countries"]["united states"] = "pages/usa.html"
index["countries"]["canada"] = "pages/ca.html"

def slugify(s):
    return str(s).lower().replace(' ', '-').replace('_', '-').replace('&', 'and')

def process_state_file(cc, state_file, filepath, include_cities=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except:
            return
            
    state_slug = slugify(state_file.replace('.json', ''))
    state_name = state_slug.replace('-', ' ')
    
    # Base URL depends on country
    if cc == 'IN':
        base_url = f"pages/in/{state_slug}"
    elif cc == 'US':
        base_url = f"pages/us/{state_slug}"
    elif cc == 'CA':
        base_url = f"pages/ca/{state_slug}"
    else:
        # Default mapping for other countries
        base_url = f"pages/{cc.lower()}/{state_slug}"
        
    # Map state
    index["states"][state_name] = f"{base_url}.html"
    
    if include_cities:
        for row in data:
            if not isinstance(row, dict): continue
            
            # Lowercase all keys for easy access
            row_lower = {k.lower(): v for k, v in row.items()}
            
            pin = str(row_lower.get('pincode', row_lower.get('zip', row_lower.get('zipcode', row_lower.get('postal_code', row_lower.get('postcode', '')))))).strip()
            city = str(row_lower.get('officename', row_lower.get('city', row_lower.get('place_name', '')))).strip()
            
            if pin and pin not in index["pincodes"]:
                city_slug = slugify(city) if city else 'unknown-city'
                index["pincodes"][pin] = f"{base_url}/{city_slug}.html"
                
            if city:
                city_key = slugify(city)
                if city_key not in index["cities"]:
                    index["cities"][city_key] = f"{base_url}/{city_key}.html"

# 1. IN
in_files = [f for f in os.listdir(data_repo) if f.endswith('.json') and f not in ('pincode-map.json', 'package.json')]
for f in in_files:
    process_state_file('IN', f, os.path.join(data_repo, f), include_cities=True)

# 2. US
us_dir = os.path.join(data_repo, 'usa')
if os.path.exists(us_dir):
    for f in os.listdir(us_dir):
        if f.endswith('.json'):
            process_state_file('US', f, os.path.join(us_dir, f), include_cities=True)

# 3. CA and World
world_dir = os.path.join(data_repo, 'world')
if os.path.exists(world_dir):
    for cc in os.listdir(world_dir):
        if cc in ('IN', 'US'): continue
        cc_dir = os.path.join(world_dir, cc)
        if os.path.isdir(cc_dir):
            for f in os.listdir(cc_dir):
                if f.endswith('.json'):
                    # Include cities/pincodes for ALL countries as requested
                    process_state_file(cc, f, os.path.join(cc_dir, f), include_cities=True)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(index, f)

print(f"Generated search index with {len(index['states'])} states, {len(index['cities'])} cities, and {len(index['pincodes'])} pincodes.")
