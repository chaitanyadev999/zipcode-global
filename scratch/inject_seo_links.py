import os
import json
import urllib.parse

base_dir = r"C:\Users\recla\zipcode-global"
data_dirs = {
    'IN': os.path.join(base_dir, 'scratch', 'pincode-dataindia'),
    'US': os.path.join(base_dir, 'scratch', 'pincode-dataindia', 'world', 'US')
}
html_files = {
    'IN': os.path.join(base_dir, 'pages', 'india.html'),
    'US': os.path.join(base_dir, 'pages', 'usa.html')
}
codes = {'IN': 'in', 'US': 'us'}

def safe_filename(name):
    if not name: return "unknown"
    return urllib.parse.quote(name.lower().replace(' ', '-').replace('/', '-'))

for cc in ['IN', 'US']:
    d_dir = data_dirs[cc]
    h_file = html_files[cc]
    code_lower = codes[cc]
    
    if not os.path.exists(h_file): continue
    if not os.path.exists(d_dir): continue
    
    links = []
    
    for file in os.listdir(d_dir):
        if not file.endswith('.json') or file == 'data.json': continue
        
        state_file = file
        state_label = file.replace('.json', '').replace('-', ' ').title()
        
        # State link
        links.append(f'<a href="/pages/{code_lower}/{state_file.replace(".json", ".html")}">{state_label}</a>')
        
        # Read JSON to get cities
        try:
            with open(os.path.join(d_dir, file), 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_field = 'City'
            if cc == 'IN': city_field = 'district'
            elif cc == 'US': city_field = 'County'
            
            cities = set()
            for row in data:
                c = row.get(city_field) or row.get('City') or row.get('district') or row.get('County')
                if c: cities.add(str(c))
                
            for city in sorted(cities):
                city_encoded = safe_filename(city)
                links.append(f'<a href="/pages/{code_lower}/{state_file.replace(".json", "")}/{city_encoded}.html">{city.title()}</a>')
        except Exception as e:
            pass

    seo_block = f'\n<!-- SEO LINKS START -->\n<div id="seo-links" style="display:none;">\n{" | ".join(links)}\n</div>\n<!-- SEO LINKS END -->\n'
    
    with open(h_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'id="seo-links"' in content:
        import re
        content = re.sub(r'<!-- SEO LINKS START -->.*?<!-- SEO LINKS END -->', seo_block, content, flags=re.DOTALL)
    else:
        content = content.replace('</body>', seo_block + '</body>')
        
    with open(h_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("SEO links injected!")
