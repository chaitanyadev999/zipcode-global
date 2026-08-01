import os
import json
import traceback
import urllib.request

SHELL_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{CITY} {TERM}, {STATE} - PO ZipCode Global</title>
<meta name="description" content="Find any {TERM} in {CITY}, {STATE}. Browse all post offices and locations with our interactive map."/>
<script>
window.PSEO_COUNTRY="{CODE}";
window.PSEO_STATE="{STATE}";
window.PSEO_CITY="{CITY}";
window.PSEO_TERM="{TERM}";
</script>
<script src="/pages/shared_pseo.js" defer></script>
<link rel="stylesheet" href="/pages/shared_pseo.css">
</head>
<body>
<div id="app"></div>
</body>
</html>'''

def clean_name(name):
    return name.lower().replace(" ", "-").replace("'", "").replace(".", "")

def generate_for_country(code, country_name, term_name):
    print(f"Generating PSEO pages for {country_name} ({code})...")
    all_urls = []
    
    api_url = f"https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/{code}"
    if code == 'IN':
        api_url = "https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/india"
    if code == 'US':
        api_url = "https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/usa"
        
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            files = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching state list: {e}")
        return []
        
    base_dir = rf"C:\Users\recla\zipcode-global\pages\{code.lower()}"
    os.makedirs(base_dir, exist_ok=True)

    for file_obj in files:
        if not file_obj['name'].endswith('.json'): continue
        if file_obj['name'] == 'regions.json': continue
        
        state_url = file_obj['name'].replace('.json', '')
        state_dir = os.path.join(base_dir, state_url)
        os.makedirs(state_dir, exist_ok=True)
        
        req_state = urllib.request.Request(file_obj['download_url'], headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req_state) as r2:
                districts = json.loads(r2.read().decode('utf-8'))
        except Exception as e:
            print(f"Failed to fetch {file_obj['name']}: {e}")
            continue
            
        for d in districts:
            if "district" not in d: continue
            city_name = d["district"]
            state_name = d.get("state", state_url.replace("-", " ").title())
            dist_url = clean_name(city_name)
            
            file_path = os.path.join(state_dir, f"{dist_url}.html")
            
            html = SHELL_TEMPLATE.replace("{CITY}", city_name).replace("{STATE}", state_name).replace("{TERM}", term_name).replace("{CODE}", code)
            
            with open(file_path, "w", encoding="utf-8") as out_f:
                out_f.write(html)
            
            all_urls.append(f"https://zipcodeglobal.github.io/pages/{code.lower()}/{state_url}/{dist_url}.html")
            
    print(f"Finished {code} -> {len(all_urls)} pages")
    return all_urls

urls_in = generate_for_country("IN", "India", "PIN Code")
urls_us = generate_for_country("US", "United States", "ZIP Code")

all_urls = (urls_in or []) + (urls_us or [])
print(f"\\nTotal generated PSEO pages: {len(all_urls)}")
