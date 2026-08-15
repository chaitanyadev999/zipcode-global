import os

pages = ['privacy.html', 'about.html', 'blog.html', 'report.html', 'translate.html']
base_dir = r'C:\Users\recla\zipcode-global\pages'

for page in pages:
    filepath = os.path.join(base_dir, page)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We want to replace href="/pages/page" with href="/pages/page" class="active"
    search_str = f'href="/pages/{page}"'
    replace_str = f'href="/pages/{page}" class="active"'
    
    if search_str in html and replace_str not in html:
        html = html.replace(search_str, replace_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Added active class to {page}')
