import os
import glob

patched = 0
for filepath in glob.glob('pages/**/*.html', recursive=True):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'shared_pseo.js"' in content:
            new_content = content.replace('shared_pseo.js"', 'shared_pseo.js?v=' + str(os.urandom(4).hex()) + '"')
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                patched += 1
    except Exception as e:
        print(f"Failed to patch {filepath}: {e}")

print(f"Patched {patched} HTML files with cache buster.")
