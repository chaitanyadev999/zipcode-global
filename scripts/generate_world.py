import urllib.request
import json
import os
import re
import urllib.parse
import time

COUNTRY_DB = {
    'IN': 'india',
    'US': 'usa',
    'AD': 'andorra', 'AE': 'united-arab-emirates', 'AI': 'anguilla', 'AL': 'albania',
    'AR': 'argentina', 'AS': 'american-samoa', 'AT': 'austria', 'AU': 'australia',
    'AX': 'aland-islands', 'AZ': 'azerbaijan', 'BD': 'bangladesh', 'BE': 'belgium',
    'BG': 'bulgaria', 'BM': 'bermuda', 'BR': 'brazil', 'BY': 'belarus', 'CA': 'canada',
    'CC': 'cocos-islands', 'CH': 'switzerland', 'CL': 'chile', 'CN': 'china',
    'CO': 'colombia', 'CR': 'costa-rica', 'CX': 'christmas-island', 'CY': 'cyprus',
    'CZ': 'czech-republic', 'DE': 'germany', 'DK': 'denmark', 'DO': 'dominican-republic',
    'DZ': 'algeria', 'EC': 'ecuador', 'EE': 'estonia', 'ES': 'spain', 'FI': 'finland',
    'FK': 'falkland-islands', 'FM': 'micronesia', 'FO': 'faroe-islands', 'FR': 'france',
    'GB': 'united-kingdom', 'GF': 'french-guiana', 'GG': 'guernsey', 'GI': 'gibraltar',
    'GL': 'greenland', 'GP': 'guadeloupe', 'GS': 'south-georgia', 'GT': 'guatemala',
    'GU': 'guam', 'HK': 'hong-kong', 'HM': 'heard-island', 'HN': 'honduras', 'HR': 'croatia',
    'HT': 'haiti', 'HU': 'hungary', 'ID': 'indonesia', 'IE': 'ireland', 'IM': 'isle-of-man',
    'IO': 'british-indian-ocean', 'IS': 'iceland', 'IT': 'italy', 'JE': 'jersey',
    'JP': 'japan', 'KE': 'kenya', 'KR': 'south-korea', 'LI': 'liechtenstein',
    'LK': 'sri-lanka', 'LT': 'lithuania', 'LU': 'luxembourg', 'LV': 'latvia',
    'MA': 'morocco', 'MC': 'monaco', 'MD': 'moldova', 'MH': 'marshall-islands',
    'MK': 'north-macedonia', 'MO': 'macao', 'MP': 'northern-mariana-islands',
    'MQ': 'martinique', 'MT': 'malta', 'MW': 'malawi', 'MX': 'mexico', 'MY': 'malaysia',
    'NC': 'new-caledonia', 'NF': 'norfolk-island', 'NL': 'netherlands', 'NO': 'norway',
    'NR': 'nauru', 'NU': 'niue', 'NZ': 'new-zealand', 'PA': 'panama', 'PE': 'peru',
    'PF': 'french-polynesia', 'PH': 'philippines', 'PK': 'pakistan', 'PL': 'poland',
    'PM': 'saint-pierre', 'PN': 'pitcairn', 'PR': 'puerto-rico', 'PT': 'portugal',
    'PW': 'palau', 'RE': 'reunion', 'RO': 'romania', 'RS': 'serbia', 'RU': 'russia',
    'SE': 'sweden', 'SG': 'singapore', 'SI': 'slovenia', 'SJ': 'svalbard',
    'SK': 'slovakia', 'SM': 'san-marino', 'TC': 'turks-and-caicos', 'TH': 'thailand',
    'TR': 'turkey', 'UA': 'ukraine', 'UY': 'uruguay', 'VA': 'vatican-city',
    'VI': 'us-virgin-islands', 'WF': 'wallis-and-futuna', 'WS': 'samoa',
    'YT': 'mayotte', 'ZA': 'south-africa'
}

def fetch_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    for _ in range(3):
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            time.sleep(2)
    return []

def get_html_shell(country_code, state_file, state_label, city_name="", depth=1):
    prefix = "../" * depth if depth > 0 else "./"
    
    country_name_pretty = COUNTRY_DB.get(country_code, country_code).replace('-', ' ').title()
    if country_code == 'US': country_name_pretty = "USA"
    if country_code == 'IN': country_name_pretty = "India"
    
    is_state = "true" if not city_name else "false"
    
    if city_name:
        title = f"{city_name.title()} Postal Codes, {state_label.title()}, {country_name_pretty} | PO ZipCode Global"
        desc = f"Find any Postal Code in {city_name.title()}, {state_label.title()}, {country_name_pretty}."
        schema_name = f"{city_name.title()} Postal Code Directory"
        city_encoded = urllib.parse.quote(city_name.lower().replace(' ', '-'))
        url = f"https://zipcodeglobal.github.io/pages/{COUNTRY_DB.get(country_code, country_code).lower()}/{state_file.replace('.json', '')}/{city_encoded}.html"
    else:
        title = f"{state_label.title()} Postal Codes, {country_name_pretty} - List of All Post Offices | PO ZipCode Global"
        desc = f"Find any Postal Code in {state_label.title()}, {country_name_pretty}. Browse all post offices and locations with our interactive map."
        schema_name = f"{state_label.title()} Postal Code Directory"
        url = f"https://zipcodeglobal.github.io/pages/{COUNTRY_DB.get(country_code, country_code).lower()}/{state_file.replace('.json', '')}.html"

    if city_name:
        seo_text = f"""
        This page provides a comprehensive list of all post offices in <strong>{city_name.title()}</strong>, located within <strong>{state_label.title()}</strong>, <strong>{country_name_pretty}</strong>. 
        Whether you are looking for delivery tracking, shipping packages, or just finding the exact postal code for your neighborhood in {city_name.title()}, you will find accurate and up-to-date information here. 
        Our global directory ensures that residents and businesses in {city_name.title()} have instant access to local postal routes and pinpoint map locations. 
        Use the interactive map above or the local search bar to quickly identify the correct ZIP or PIN code for your specific area.
        """
    else:
        seo_text = f"""
        Explore the complete directory of postal codes and post offices across <strong>{state_label.title()}</strong>, <strong>{country_name_pretty}</strong>. 
        This directory is designed to help you quickly find accurate ZIP codes, PIN codes, and postal information for all regions within {state_label.title()}. 
        From major metropolitan areas to remote districts in {state_label.title()}, our database ensures seamless mail delivery and geographical lookup. 
        Each entry provides precise latitude and longitude coordinates for map integration. 
        Select a city or use the local search tool to narrow down your results instantly.
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{schema_name}",
  "description": "{desc}",
  "url": "{url}"
}}
</script>
<script>
window.PSEO_COUNTRY="{country_code}";
window.PSEO_STATE="{state_file}";
window.PSEO_STATE_LABEL="{state_label}";
window.PSEO_CITY="{city_name}";
window.PSEO_IS_STATE={is_state};
</script>
<link rel="stylesheet" href="{prefix}shared_pseo.css?v=1.2">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<style>
  .seo-text {{ padding: 20px; background: rgba(255,255,255,0.05); margin: 20px auto; max-width: 800px; border-radius: 8px; color: #ccc; line-height: 1.6; text-align: center; font-size: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); }}
  @media (max-width: 768px) {{ .seo-text {{ margin: 10px; padding: 15px; font-size: 13px; }} }}
</style>
</head>
<body>
<div id="app"></div>
<div class="seo-text">
{seo_text}
</div>
<script src="{prefix}shared_pseo.js?v=1.2"></script>
</body>
</html>"""
    return html

def safe_name(name):
    return urllib.parse.quote(re.sub(r'[^a-zA-Z0-9]', '-', str(name).strip().lower()))

def process_country(country_code, url):
    print(f"Fetching {country_code} states...")
    states = fetch_json(url)
    if not states:
        return
        
    country_folder_name = COUNTRY_DB.get(country_code, country_code.lower())
    base_dir = os.path.join(os.getcwd(), 'pages', country_folder_name)
    os.makedirs(base_dir, exist_ok=True)
    
    total_states = 0
    total_cities = 0
    
    for state in states:
        if not state['name'].endswith('.json') or state['name'] == 'data.json':
            continue
            
        state_file = state['name']
        state_label = state_file.replace('.json', '').replace('-', ' ')
        
        state_html = get_html_shell(country_code, state_file, state_label, depth=1)
        state_path = os.path.join(base_dir, state_file.replace('.json', '.html'))
        with open(state_path, "w", encoding="utf-8") as f:
            f.write(state_html)
        total_states += 1
        
        raw_url = state['download_url']
        state_data = fetch_json(raw_url)
        if not state_data:
            continue
            
        cities = set()
        for item in state_data:
            if not isinstance(item, dict): continue
            c = item.get('officename') or item.get('OfficeName') or item.get('City')
            if c:
                clean = re.sub(r'(?i)\s+(b\.o|s\.o|h\.o|bo|so|ho)$', '', str(c))
                cities.add(clean.strip())
                
        city_dir = os.path.join(base_dir, state_file.replace('.json', ''))
        os.makedirs(city_dir, exist_ok=True)
        
        for city in cities:
            city_safe = safe_name(city)
            if not city_safe: continue
            
            city_html = get_html_shell(country_code, state_file, state_label, city_name=city, depth=2)
            city_path = os.path.join(city_dir, city_safe + '.html')
            with open(city_path, "w", encoding="utf-8") as f:
                f.write(city_html)
            total_cities += 1
            
    print(f"[{country_code}] Generated {total_states} states and {total_cities} cities.")

def main():
    for code, name in COUNTRY_DB.items():
        if code == 'IN':
            process_country(code, "https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/")
        else:
            process_country(code, f"https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/{code}")

if __name__ == "__main__":
    main()
    # Only test Canada for now since India and USA take too long sequentially without async.
    process_country("CA", "https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/CA")
    
if __name__ == "__main__":
    main()


