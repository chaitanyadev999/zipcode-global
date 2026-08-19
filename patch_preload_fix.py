import os
import glob

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # Fix 1: push(...data) to concat(data)
        if 'window.globalDataCache.push(...data);' in content:
            content = content.replace('window.globalDataCache.push(...data);', 'window.globalDataCache = window.globalDataCache.concat(data);')
            modified = True
            
        # Fix 2: Add delay between batches to unblock main thread
        batch_await = 'await Promise.all(batch.map(async (url) => {'
        if batch_await in content and 'await new Promise(r => setTimeout(r, 150));' not in content:
            content = content.replace(batch_await, 'await new Promise(r => setTimeout(r, 150)); // Yield to main thread\n                ' + batch_await)
            modified = True
            
        # Fix 3: Delay the initial execution of preloadGlobalData
        if 'loadStates();\npreloadGlobalData();' in content:
            content = content.replace('loadStates();\npreloadGlobalData();', 'loadStates();\nsetTimeout(preloadGlobalData, 4000);')
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"Error on {filepath}: {e}")
    return False

# Fix generate_pages.py
if fix_file('generate_pages.py'):
    print("Fixed generate_pages.py")

# Fix pages/*.html
patched_count = 0
for file in glob.glob('pages/*.html'):
    if fix_file(file):
        patched_count += 1

print(f"Fixed {patched_count} HTML files in pages/ directory.")
