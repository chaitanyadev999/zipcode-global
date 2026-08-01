import urllib.request
import json
import os
import re

def fetch_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))

def generate_state_shell(country_code, state_file, state_label, depth=1):
    prefix = "../" * depth if depth > 0 else "./"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{state_label.title()} Postal Codes, {country_code} - List of All Post Offices | PO ZipCode Global</title>
<meta name="description" content="Find any Postal Code in {state_label.title()}, {country_code}. Browse all post offices and locations with our interactive map.">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{state_label.title()} Postal Code Directory",
  "description": "Comprehensive Postal Code directory for {state_label.title()}, {country_code}.",
  "url": "https://zipcodeglobal.github.io/pages/{country_code.lower()}/{state_file.replace('.json', '')}.html"
}}
</script>
<script>
window.PSEO_COUNTRY="{country_code}";
window.PSEO_STATE="{state_file}";
window.PSEO_STATE_LABEL="{state_label}";
window.PSEO_CITY="";
window.PSEO_IS_STATE=true;
</script>
<link rel="stylesheet" href="{prefix}shared_pseo.css?v=1.1">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<style>
  .seo-text {{ padding: 20px; background: rgba(255,255,255,0.05); margin: 20px auto; max-width: 800px; border-radius: 8px; color: #ccc; line-height: 1.6; text-align: center; font-size: 14px; }}
  @media (max-width: 768px) {{ .seo-text {{ margin: 10px; padding: 15px; font-size: 13px; }} }}
</style>
</head>
<body>
<div id="app"></div>
<div class="seo-text">
</div>
<script src="{prefix}shared_pseo.js?v=1.1"></script>
</body>
</html>"""
    return html

def process_country(country_code, url):
    print(f"Fetching {country_code} states...")
    try:
        states = fetch_json(url)
    except Exception as e:
        print(f"Failed to fetch {country_code} states", e)
        return

    base_dir = os.path.join(os.getcwd(), 'pages', country_code.lower())
    os.makedirs(base_dir, exist_ok=True)
    
    total = 0
    for state in states:
        if not state['name'].endswith('.json') or state['name'] == 'data.json':
            continue
            
        state_file = state['name']
        state_label = state_file.replace('.json', '').replace('-', ' ')
        
        html = generate_state_shell(country_code, state_file, state_label, depth=1)
        
        file_path = os.path.join(base_dir, state_file.replace('.json', '.html'))
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        total += 1
        print(f"Generated state page for {state_label} in {country_code}")
        
    print(f"Total state pages generated for {country_code}: {total}")

def main():
    process_country("IN", "https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/")
    process_country("US", "https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/US")
    process_country("CA", "https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/CA")
    
if __name__ == "__main__":
    main()
