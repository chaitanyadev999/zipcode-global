import os
import re

old_domain = "https://zipcodeglobal.github.io"
new_domain = "https://chaitanyadev999.github.io/pincode-dataindia"

base_dir = r'C:\Users\recla\zipcode-global'
count = 0

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(('.html', '.js', '.json', '.xml')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if old_domain in content or 'zipcodeglobal.github.io' in content:
                    content = content.replace(old_domain, new_domain)
                    # Also replace bare domain just in case
                    content = content.replace('zipcodeglobal.github.io', 'chaitanyadev999.github.io/pincode-dataindia')
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
            except Exception as e:
                print(f"Error reading {filepath}: {e}")

print(f"Replaced domain in {count} files.")
