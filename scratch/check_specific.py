import os

base_dir = r'C:\Users\recla\zipcode-global'
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if 'href="/pages/usa/Tennessee/coffee.html"' in content:
                    print(f"File: {filepath}")
            except:
                pass
