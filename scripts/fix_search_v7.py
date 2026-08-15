import os
import json
import sys
import re

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
    s = name.lower().replace(" ", "-")
    s = re.sub(r'[^a-z0-9\-]', '', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')

cc_to_slug = {}
for c in COUNTRIES:
    cc_to_slug[c[0]] = slugify(c[1])

sitemap_file = r"C:\Users\recla\zipcode-global\sitemap_cities.txt"
valid_urls = set()
with open(sitemap_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line: continue
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
    country_page = f"pages/{country_slug}.html"
    
    index["states"][state_name] = f"{base_url}.html"
    
    for row in data:
        if not isinstance(row, dict): continue
        row_lower = {k.lower(): v for k, v in row.items()}
        pin = str(row_lower.get('pincode', row_lower.get('zip', row_lower.get('zipcode', row_lower.get('postal_code', row_lower.get('postcode', '')))))).strip()
        
        officename = str(row_lower.get('officename', row_lower.get('place_name', row_lower.get('city', '')))).strip()
        district = str(row_lower.get('districtname', row_lower.get('district', ''))).strip()
        city = str(row_lower.get('city', '')).strip()
        
        # Build candidates
        names_to_try = []
        if officename:
            names_to_try.append(officename)
            stripped = re.sub(r'(?i)\b(b\.o|s\.o|h\.o|bo|so|ho)\b', '', officename).strip()
            if stripped: names_to_try.append(stripped)
        if district: names_to_try.append(district)
        if city: names_to_try.append(city)
        
        target_url = None
        for n in names_to_try:
            if not n: continue
            candidate_slug = clean_name(n)
            candidate_url = f"{base_url}/{candidate_slug}.html"
            if candidate_url in valid_urls:
                target_url = candidate_url
                break
                
        # If SEO page does not exist on disk, redirect to Country page with ?q= query string
        if not target_url:
            if pin:
                target_url_pin = f"{country_page}?q={pin}"
            if officename:
                target_url_city = f"{country_page}?q={clean_name(officename)}"
            elif district:
                target_url_city = f"{country_page}?q={clean_name(district)}"
            else:
                target_url_city = None
        else:
            target_url_pin = target_url
            target_url_city = target_url
            
        if pin and pin not in index["pincodes"]:
            index["pincodes"][pin.lower()] = target_url_pin or f"{country_page}?q={pin}"
            
        if officename:
            city_key = officename.lower()
            if city_key not in index["cities"] and target_url_city:
                index["cities"][city_key] = target_url_city
        if district:
            dist_key = district.lower()
            if dist_key not in index["cities"] and target_url_city:
                index["cities"][dist_key] = target_url_city

print("Generating ultra-smart search index...")
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

print(f"Generated ultra-smart index! {len(index['pincodes'])} pincodes mapped safely.")
