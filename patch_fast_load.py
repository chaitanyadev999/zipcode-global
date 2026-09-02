import os
import re

pages_dir = r"C:\Users\recla\zipcode-global\pages"

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content

    # 1. Fix the "All Countries" link
    content = content.replace('href="/home/main.html">&#8592; All Countries', 'href="/">&#8592; All Countries')
    
    # 2. Replace GitHub API fetching with tree.json logic
    # Find block starting with const apiUrl = ... and ending with const files = await r.json();
    pattern1 = r"const apiUrl = C\.code === 'IN'\s*\?[^;]+;\s*const r = await fetch\(apiUrl\);\s*if\(!r\.ok\) throw new Error\(r\.status\);\s*const files = await r\.json\(\);"
    
    replacement1 = """const r = await fetch('/tree.json');
      if(!r.ok) throw new Error(r.status);
      const treeData = await r.json();
      const prefix = C.code === 'IN' ? '' : 'world/' + C.code + '/';
      const files = treeData.tree.filter(f => f.path.startsWith(prefix) && f.path.endsWith('.json') && (C.code !== 'IN' || !f.path.includes('/'))).map(f => {
          return { name: f.path.split('/').pop(), download_url: 'https://cdn.jsdelivr.net/gh/chaitanyadev999/pincode-dataindia@main/' + f.path };
      });"""
      
    content = re.sub(pattern1, replacement1, content)
    
    # Pattern for preloadGlobalData (uses if(r.ok) { ... )
    pattern2 = r"const apiUrl = C\.code === 'IN'\s*\?[^;]+;\s*const r = await fetch\(apiUrl\);\s*if\(r\.ok\)\s*\{\s*const files = await r\.json\(\);"
    
    replacement2 = """const r = await fetch('/tree.json');
          if(r.ok) {
              const treeData = await r.json();
              const prefix = C.code === 'IN' ? '' : 'world/' + C.code + '/';
              const files = treeData.tree.filter(f => f.path.startsWith(prefix) && f.path.endsWith('.json') && (C.code !== 'IN' || !f.path.includes('/'))).map(f => {
                  return { name: f.path.split('/').pop(), download_url: 'https://cdn.jsdelivr.net/gh/chaitanyadev999/pincode-dataindia@main/' + f.path };
              });"""
              
    content = re.sub(pattern2, replacement2, content)

    # 3. Speed up downloads by batching 10 at a time instead of 5, and reducing timeout
    content = content.replace('i < jsonUrls.length; i += 5', 'i < jsonUrls.length; i += 15')
    content = content.replace('jsonUrls.slice(i, i + 5)', 'jsonUrls.slice(i, i + 15)')
    content = content.replace('setTimeout(r, 150)', 'setTimeout(r, 20)')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for file in os.listdir(pages_dir):
    if file.endswith('.html'):
        filepath = os.path.join(pages_dir, file)
        if os.path.isfile(filepath):
            if patch_file(filepath):
                count += 1

print(f"Patched fast loading and All Countries link in {count} files.")
