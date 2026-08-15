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
    
    # frontend state key logic: q.replace(/[^a-z0-9\s-]/g, '').trim().replace(/\s+/g, ' ');
    state_key = re.sub(r'[^a-z0-9\s-]', '', state_name).strip().replace('-', ' ')
    state_key = re.sub(r'\s+', ' ', state_key)
    index["states"][state_key] = f"{base_url}.html"
    
    for row in data:
        if not isinstance(row, dict): continue
        row_lower = {k.lower(): v for k, v in row.items()}
        pin = str(row_lower.get('pincode', row_lower.get('zip', row_lower.get('zipcode', row_lower.get('postal_code', row_lower.get('postcode', '')))))).strip()
        
        officename = str(row_lower.get('officename', row_lower.get('place_name', row_lower.get('city', '')))).strip()
        district = str(row_lower.get('districtname', row_lower.get('district', ''))).strip()
        city = str(row_lower.get('city', '')).strip()
        
        target_url_city = None
        target_url_dist = None
        target_url_pin = None

        if officename:
            candidate_slug = clean_name(officename)
            if f"{base_url}/{candidate_slug}.html" in valid_urls:
                target_url_city = f"{base_url}/{candidate_slug}.html"
            else:
                target_url_city = f"{country_page}?q={candidate_slug}"
                
        if district:
            candidate_slug = clean_name(district)
            if f"{base_url}/{candidate_slug}.html" in valid_urls:
                target_url_dist = f"{base_url}/{candidate_slug}.html"
            else:
                target_url_dist = f"{country_page}?q={candidate_slug}"

        if pin:
            target_url_pin = target_url_city if (target_url_city and '?' not in target_url_city) else f"{country_page}?q={pin}"

        if pin and pin not in index["pincodes"]:
            index["pincodes"][pin.lower()] = target_url_pin
            
        if officename:
            # Match frontend logic
            city_key = clean_name(officename)
            if city_key and city_key not in index["cities"] and target_url_city:
                index["cities"][city_key] = target_url_city
                
            # Also index without suffixes to help users who just type 'thimmaparam' instead of 'thimmaparam bo'
            stripped = re.sub(r'(?i)\b(b\.o|s\.o|h\.o|bo|so|ho)\b', '', officename).strip()
            if stripped:
                city_key_stripped = clean_name(stripped)
                if city_key_stripped and city_key_stripped not in index["cities"] and target_url_city:
                    index["cities"][city_key_stripped] = target_url_city
                
        if district:
            dist_key = clean_name(district)
            if dist_key and dist_key not in index["cities"] and target_url_dist:
                index["cities"][dist_key] = target_url_dist
                
        if city:
            c_key = clean_name(city)
            if c_key and c_key not in index["cities"]:
                candidate_slug = clean_name(city)
                if f"{base_url}/{candidate_slug}.html" in valid_urls:
                    index["cities"][c_key] = f"{base_url}/{candidate_slug}.html"
                else:
                    index["cities"][c_key] = f"{country_page}?q={candidate_slug}"

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
