import os
import re

base_dir = r'C:\Users\recla\zipcode-global'
pattern = re.compile(r'href=[\'"](https?://(chaitanyadev999|zipcodeglobal)\.github\.io[^(\'")]*)[\'"]')
found = False
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                matches = pattern.findall(content)
                if matches:
                    print(f"File: {filepath}")
                    for m in matches:
                        print(f"  -> {m[0]}")
                    found = True
                    break # just show the first file for now
            except:
                pass
    if found:
        break
print("Search done.")
