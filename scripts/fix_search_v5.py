import os
import json
import sys

# Extract COUNTRIES
sys.path.append(r"C:\Users\recla\zipcode-global")
try:
    import generate_pages
    COUNTRIES = generate_pages.COUNTRIES
except Exception as e:
    print(f"Error importing COUNTRIES: {e}")
    sys.exit(1)

def slugify(s):
    return str(s).lower().replace(' ', '-').replace('_', '-').replace('&', 'and')

def clean_name(name):
    # This was the exact function used in generate_city_seo.py
    return name.lower().replace(" ", "-").replace("'", "").replace(".", "")

cc_to_slug = {}
for c in COUNTRIES:
    cc_to_slug[c[0]] = slugify(c[1])

# 1. Load valid URLs from sitemap
sitemap_file = r"C:\Users\recla\zipcode-global\sitemap_cities.txt"
valid_urls = set()
with open(sitemap_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        # https://zipcodeglobal.github.io/pages/india/andhra-pradesh/gandhinagaram-so-vijayawada.html
        url_path = line.replace("https://zipcodeglobal.github.io/", "")
        valid_urls.add(url_path)

data_repo = r"C:\Users\recla\zipcode-global\scratch\pincode-dataindia"
output_file = r"C:\Users\recla\zipcode-global\home\assets\search_index.json"

index = {
    "countries": {},
    "states": {},
    "cities": {},
    "pincodes": {}
}

for c in COUNTRIES:
    slug = slugify(c[1])
    index["countries"][c[1].lower()] = f"pages/{slug}.html"
index["countries"]["united states"] = "pages/united-states.html"
index["countries"]["usa"] = "pages/united-states.html"
index["countries"]["uk"] = "pages/united-kingdom.html"

def process_state_file(cc, state_file, filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except:
            return
            
    state_slug = slugify(state_file.replace('.json', ''))
    state_name = state_slug.replace('-', ' ')
    country_slug = cc_to_slug.get(cc, cc.lower())
    base_url = f"pages/{country_slug}/{state_slug}"
    
    index["states"][state_name] = f"{base_url}.html"
    
    for row in data:
        if not isinstance(row, dict): continue
        row_lower = {k.lower(): v for k, v in row.items()}
        pin = str(row_lower.get('pincode', row_lower.get('zip', row_lower.get('zipcode', row_lower.get('postal_code', row_lower.get('postcode', '')))))).strip()
        
        # Priority for the SEO page was likely district, let's check what was used. 
        # Actually generate_city_seo.py used d["district"] from the state JSON files!
        # But wait, we can just check if clean_name(officename) exists in valid_urls!
        officename = str(row_lower.get('officename', row_lower.get('place_name', row_lower.get('city', '')))).strip()
        district = str(row_lower.get('districtname', row_lower.get('district', ''))).strip()
        city = str(row_lower.get('city', '')).strip()
        
        target_url = None
        names_to_try = [officename, district, city]
        
        # Try to find which one actually has an HTML file generated
        for n in names_to_try:
            if not n: continue
            candidate_slug = clean_name(n)
            candidate_url = f"{base_url}/{candidate_slug}.html"
            if candidate_url in valid_urls:
                target_url = candidate_url
                break
                
        # If none matched, just fallback to clean_name(officename) hoping it's correct but maybe not in sitemap
        if not target_url:
            candidate_slug = clean_name(officename) if officename else 'unknown'
            target_url = f"{base_url}/{candidate_slug}.html"
            
        if pin and pin not in index["pincodes"]:
            index["pincodes"][pin.lower()] = target_url
            
        if officename:
            city_key = officename.lower()
            if city_key not in index["cities"]:
                index["cities"][city_key] = target_url
        if district:
            dist_key = district.lower()
            if dist_key not in index["cities"]:
                index["cities"][dist_key] = target_url

print("Generating smart search index...")
in_files = [f for f in os.listdir(data_repo) if f.endswith('.json') and f not in ('pincode-map.json', 'package.json')]
for f in in_files:
    process_state_file('IN', f, os.path.join(data_repo, f))

us_dir = os.path.join(data_repo, 'usa')
if os.path.exists(us_dir):
    for f in os.listdir(us_dir):
        if f.endswith('.json'): process_state_file('US', f, os.path.join(us_dir, f))

world_dir = os.path.join(data_repo, 'world')
if os.path.exists(world_dir):
    for cc in os.listdir(world_dir):
        if cc in ('IN', 'US'): continue
        cc_dir = os.path.join(world_dir, cc)
        if os.path.isdir(cc_dir):
            for f in os.listdir(cc_dir):
                if f.endswith('.json'):
                    process_state_file(cc, f, os.path.join(cc_dir, f))

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(index, f)

print(f"Generated smart index! {len(index['pincodes'])} pincodes mapped securely.")
