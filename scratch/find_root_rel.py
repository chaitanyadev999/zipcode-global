import os
import re

base_dir = r'C:\Users\recla\zipcode-global'
pattern = re.compile(r'href=[\'"](/[^"\'\n]+)[\'"]')
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
                    for m in set(matches):
                        print(f"  -> {m}")
            except:
                pass
