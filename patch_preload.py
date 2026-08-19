import os
import glob

# The preload function to add
preload_fn = """
async function preloadGlobalData() {
    if(window.globalDataCache || window.isFetchingGlobal) return;
    window.isFetchingGlobal = true;
    window.globalDataCache = [];
    try {
        const apiUrl = C.code === 'IN' ? 'https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents' : 'https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/'+C.code;
        const r = await fetch(apiUrl);
        if(r.ok) {
            const files = await r.json();
            const jsonUrls = files.filter(f=>f.name.endsWith('.json') && f.name !== 'pincode-map.json' && f.name !== 'package.json' && f.name !== 'data.json').map(f=>f.download_url);
            for (let i = 0; i < jsonUrls.length; i += 5) {
                const batch = jsonUrls.slice(i, i + 5);
                await Promise.all(batch.map(async (url) => {
                    try {
                        const dr = await fetch(url);
                        if(dr.ok) {
                            const data = await dr.json();
                            window.globalDataCache.push(...data);
                        }
                    } catch(e) {}
                }));
            }
        }
    } catch(e) {}
    window.isFetchingGlobal = false;
}
"""

def patch_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # Add preloadGlobalData function if not present
        if 'async function preloadGlobalData' not in content:
            # Insert before doSearch
            content = content.replace('async function doSearch', preload_fn + '\nasync function doSearch')
            modified = True
            
        # Add preloadGlobalData(); call at the bottom
        if 'loadStates();' in content and 'preloadGlobalData();' not in content:
            content = content.replace('loadStates();', 'loadStates();\npreloadGlobalData();')
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"Error on {filepath}: {e}")
    return False

# Patch generate_pages.py
if patch_file('generate_pages.py'):
    print("Patched generate_pages.py")

# Patch pages/*.html
patched_count = 0
for file in glob.glob('pages/*.html'):
    if patch_file(file):
        patched_count += 1

print(f"Patched {patched_count} HTML files in pages/ directory.")
