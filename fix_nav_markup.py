import os
import re

pages = ['privacy.html', 'about.html', 'blog.html', 'report.html', 'translate.html']
base_dir = r'C:\Users\recla\zipcode-global\pages'

for page in pages:
    filepath = os.path.join(base_dir, page)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Replace nav and container
    html = html.replace('<nav class="cinema-nav">\n  <div class="container" style="display:flex; justify-content:space-between; align-items:center;">', '<nav class="nav" id="mainNav">')
    html = html.replace('<nav class="cinema-nav">\n    <div class="container" style="display:flex; justify-content:space-between; align-items:center;">', '<nav class="nav" id="mainNav">')
    html = html.replace('<nav class="cinema-nav">\n<div class="container" style="display:flex; justify-content:space-between; align-items:center;">', '<nav class="nav" id="mainNav">')
    html = html.replace('<nav class="cinema-nav">\n  <div class="container" style="display: flex; justify-content: space-between; align-items: center;">', '<nav class="nav" id="mainNav">')
    
    # Also just in case it's in one line
    html = re.sub(r'<nav class="cinema-nav">\s*<div class="container"[^>]*>', '<nav class="nav" id="mainNav">', html)

    # 2. Replace brand-icon with bmark
    html = html.replace('class="brand-icon"', 'class="bmark"')

    # 3. Remove the extra closing div for the container before </nav>
    html = re.sub(r'    </div>\s*</nav>', '    </nav>', html)
    html = re.sub(r'  </div>\s*</nav>', '</nav>', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated {page}')
