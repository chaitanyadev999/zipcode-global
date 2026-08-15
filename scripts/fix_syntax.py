import os

pages_dir = r"C:\Users\recla\zipcode-global\pages"
updated = 0

for file in os.listdir(pages_dir):
    if not file.endswith('.html'): continue
    
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check for the double IIFE closing
    if '})();})();' in html:
        html = html.replace('})();})();', '})();')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        updated += 1

print(f"Fixed syntax error in {updated} files.")
