import glob
import re

files = ['index.html'] + glob.glob('pages/*.html')

favicon_tag = '<link rel="icon" type="image/png" href="/home/assets/logo.png">'

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if favicon exists
    if '<link rel="icon"' in content:
        # Replace existing
        content = re.sub(r'<link rel="icon"[^>]+>', favicon_tag, content)
    else:
        # Insert it
        content = content.replace('</title>', '</title>\n' + favicon_tag)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Favicon updated on all pages.')
