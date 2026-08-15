import os
import json
import re

pages_dir = r"C:\Users\recla\zipcode-global\pages"
data_repo = r"C:\Users\recla\zipcode-global\scratch\pincode-dataindia"

states_map = {}

# IN
if os.path.exists(data_repo):
    in_files = [f for f in os.listdir(data_repo) if f.endswith('.json') and f not in ('pincode-map.json', 'package.json')]
    states_map['IN'] = [{'name': f} for f in in_files]

# US
us_dir = os.path.join(data_repo, 'usa')
if os.path.exists(us_dir):
    us_files = [f for f in os.listdir(us_dir) if f.endswith('.json')]
    states_map['US'] = [{'name': f} for f in us_files]

# World
world_dir = os.path.join(data_repo, 'world')
if os.path.exists(world_dir):
    for cc in os.listdir(world_dir):
        cc_dir = os.path.join(world_dir, cc)
        if os.path.isdir(cc_dir):
            files = [f for f in os.listdir(cc_dir) if f.endswith('.json')]
            states_map[cc] = [{'name': f} for f in files]

updated = 0
for file in os.listdir(pages_dir):
    if not file.endswith('.html'): continue
    if file == 'country-template.html': continue
    
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    m = re.search(r"code\s*:\s*'([A-Z]{2})'", html)
    if not m: continue
    cc = m.group(1)
    
    if cc not in states_map:
        continue
    
    states_json = json.dumps(states_map[cc])
    new_logic = f"""// Fetch bypassed
    const states = {states_json};"""
    
    pattern = re.compile(r"const apiUrl = [^;]+;\s*const r = await fetch\(apiUrl\);\s*if\(!r\.ok\)[^;]+;\s*const files = await r\.json\(\);\s*const states = files\.filter\([^;]+;\s*", re.MULTILINE)
    match = pattern.search(html)
    
    if match:
        old_text = match.group(0)
        new_html = html.replace(old_text, new_logic + "\n    ")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        updated += 1

print(f"Updated {updated} files.")
