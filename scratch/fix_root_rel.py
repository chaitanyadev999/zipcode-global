import os
import re

base_dir = r'C:\Users\recla\zipcode-global\pages'
count = 0

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            # Calculate depth relative to zipcode-global root
            # root is like .../zipcode-global/pages (depth 1)
            # or .../zipcode-global/pages/india (depth 2)
            rel_path = os.path.relpath(filepath, r'C:\Users\recla\zipcode-global')
            depth = rel_path.count(os.sep)
            
            root_prefix = '../' * depth
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                
                # Replace specific known root relative paths
                content = content.replace('src="/home/assets/logo.png"', f'src="{root_prefix}home/assets/logo.png"')
                content = content.replace('href="/"', f'href="{root_prefix}home/main.html"')
                content = content.replace('href="/#countriesSection"', f'href="{root_prefix}home/main.html#allSec"')
                content = content.replace('href="/pages/report.html', f'href="{root_prefix}pages/report.html')
                
                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
            except Exception as e:
                print(f"Error {filepath}: {e}")

print(f"Fixed root relative links in {count} HTML files.")
