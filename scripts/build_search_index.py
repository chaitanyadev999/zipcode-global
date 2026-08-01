import urllib.request
import json
import os
import re
import time

def fetch_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))

def safe_filename(name):
    if not name: return 'unknown'
    name = re.sub(r'[^a-zA-Z0-9\s-]', '', str(name))
    name = name.strip().lower().replace(' ', '-')
    return name

index = {
    "cities": {},
    "states": {},
    "pincodes": {}
}

def process_country(country_code, base_url, json_url_prefix):
    print(f"Building search index for {country_code}...")
    try:
        states = fetch_json(base_url)
    except Exception as e:
        print(f"Failed to fetch {country_code} states", e)
        return

    c_code = country_code.lower()

    for state in states:
        if not state['name'].endswith('.json') or state['name'] == 'data.json':
            continue
            
        state_file = state['name']
        state_label = state_file.replace('.json', '').replace('-', ' ')
        state_safe = safe_filename(state_label)
        
        # Add state to index
        index["states"][state_label.lower()] = f"pages/{c_code}/{state_file.replace('.json', '.html')}"
        
        # Fetch state data to get cities and pincodes
        state_data_url = f"{json_url_prefix}/{state_file}"
        try:
            data = fetch_json(state_data_url)
        except Exception as e:
            print(f"Failed to fetch data for {state_file}: {e}")
            continue
            
        if not isinstance(data, list):
            continue
        for item in data:
            if not isinstance(item, dict):
                continue
            city = item.get('district') or item.get('City') or item.get('regionname') or ''
            city = str(city).strip()
            
            pincode = str(item.get('pincode') or item.get('ZipCode') or item.get('zipcode') or '').strip()
            
            if city and len(city) > 1:
                city_key = city.lower()
                city_safe = safe_filename(city)
                target_url = f"pages/{c_code}/{state_safe}/{city_safe}.html"
                
                # We want to keep the mapping. We can just overwrite if duplicates.
                if city_key not in index["cities"]:
                    index["cities"][city_key] = target_url
                    
                if pincode and pincode != 'None' and pincode not in index["pincodes"]:
                    index["pincodes"][pincode] = target_url

def main():
    print("Starting index build...")
    # IN
    process_country("IN", 
                   "https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/", 
                   "https://raw.githubusercontent.com/chaitanyadev999/pincode-dataindia/master")
    # US
    process_country("US", 
                   "https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/US", 
                   "https://raw.githubusercontent.com/chaitanyadev999/pincode-dataindia/master/world/US")
    # CA
    process_country("CA", 
                   "https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/CA", 
                   "https://raw.githubusercontent.com/chaitanyadev999/pincode-dataindia/master/world/CA")
                   
    out_dir = os.path.join(os.getcwd(), 'home', 'assets')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'search_index.json')
    
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, separators=(',', ':'))
        
    print(f"Index built successfully! Saved to {out_file}")
    print(f"Stats:")
    print(f"- States: {len(index['states'])}")
    print(f"- Cities: {len(index['cities'])}")
    print(f"- Pincodes: {len(index['pincodes'])}")
    print(f"- File size: {os.path.getsize(out_file) / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    main()

