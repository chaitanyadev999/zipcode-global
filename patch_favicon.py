import os

pages_dir = r"C:\Users\recla\zipcode-global\pages"
favicon_tag = '<link rel="icon" type="image/png" href="/home/assets/logo.png">\n'

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content

    if '<link rel="icon"' not in content:
        content = content.replace('<head>\n', '<head>\n' + favicon_tag)
        
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

print(f"Added favicon to {count} files.")
