import os
import glob

html_files = glob.glob('pages/*.html')

old_city = "f.city = keys.find(k=>k==='city'||k.includes('division')||k.includes('municipality')||k.includes('suburb'));"
new_city = "f.city = keys.find(k=>k==='city'||k==='officename'||k.includes('division')||k.includes('municipality')||k.includes('suburb'));"

old_listener = "$('search').addEventListener('keypress',e=>{if(e.key==='Enter')doSearch();});"
new_listener = "$('search').addEventListener('keypress',e=>{if(e.key==='Enter')doSearch();});\nlet searchTo=null;\n$('search').addEventListener('input',e=>{clearTimeout(searchTo);searchTo=setTimeout(doSearch,400);});"

patched_count = 0

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        if old_city in content:
            content = content.replace(old_city, new_city)
            modified = True
            
        if old_listener in content:
            content = content.replace(old_listener, new_listener)
            modified = True
            
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            patched_count += 1
            
    except Exception as e:
        print(f"Error on {file}: {e}")

print(f"Patched {patched_count} HTML files in pages/ directory.")
