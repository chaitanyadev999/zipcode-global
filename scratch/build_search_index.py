import os
import json
import re

base_dir = r'C:\Users\recla\zipcode-global'
data_dir = os.path.join(base_dir, 'home', 'data')
pages_dir = os.path.join(base_dir, 'pages')

index = {
    'countries': {},
    'states': {},
    'cities': {},
    'pincodes': {}
}

def clean_key(s):
    return re.sub(r'[^a-z0-9\s-]', '', str(s).lower()).strip().replace(' ', '-')

# Map countries
try:
    for f in os.listdir(data_dir):
        if f.endswith('.json'):
            country = f.replace('.json', '')
            country_slug = clean_key(country)
            if country_slug == 'in': country_slug = 'india'
            if country_slug == 'us': country_slug = 'usa'
            index['countries'][country_slug] = f'pages/{country_slug}.html'
except FileNotFoundError:
    print(f"Data dir {data_dir} not found. Skipping country map from data dir.")
    # Fallback to pages dir for countries
    for f in os.listdir(pages_dir):
        if f.endswith('.html') and not f.startswith('shared'):
            country = f.replace('.html', '')
            country_slug = clean_key(country)
            index['countries'][country_slug] = f'pages/{country_slug}.html'

print('Mapping states and cities for all countries from pages HTML files...')
# Crawl the pages/ folder to build exact paths to HTML files
for country_slug in os.listdir(pages_dir):
    country_path = os.path.join(pages_dir, country_slug)
    if os.path.isdir(country_path):
        for state_slug in os.listdir(country_path):
            state_path = os.path.join(country_path, state_slug)
            if os.path.isdir(state_path):
                # Add state
                index['states'][state_slug] = f'pages/{country_slug}/{state_slug}.html'
                
                # Add cities/pincodes within state
                for file in os.listdir(state_path):
                    if file.endswith('.html'):
                        name = file.replace('.html', '')
                        if name == state_slug: continue # Skip the state index file if present
                        
                        file_path = f'pages/{country_slug}/{state_slug}/{file}'
                        
                        # Is it a pincode?
                        if re.match(r'^\d+$', name):
                            index['pincodes'][name] = file_path
                        else:
                            index['cities'][name] = file_path

# Save index
out_path = os.path.join(base_dir, 'home', 'assets', 'search_index.json')
print(f"Saving to {out_path}...")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(index, f, separators=(',', ':'))

print(f'Done! Indexed {len(index["countries"])} countries, {len(index["states"])} states, {len(index["cities"])} cities, {len(index["pincodes"])} pincodes.')
