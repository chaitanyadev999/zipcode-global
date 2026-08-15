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
    
    # Standardize the HTML class for the logo div to brand-icon
    html = html.replace('<div class="bmark">', '<div class="brand-icon">')
    html = html.replace('<div class="brand-mark">', '<div class="brand-icon">')
    
    # Standardize the CSS class name
    html = html.replace('.bmark {', '.brand-icon {')
    html = html.replace('.bmark{', '.brand-icon{')
    html = html.replace('.bmark img', '.brand-icon img')
    html = html.replace('.brand-mark {', '.brand-icon {')
    html = html.replace('.brand-mark{', '.brand-icon{')
    html = html.replace('.brand-mark img', '.brand-icon img')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Standardized {page}')
