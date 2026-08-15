import os
import re

filepath = r"C:\Users\recla\zipcode-global\pages\blog.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

links = re.findall(r'href="(blog/[^"]+)"', html)
base_dir = r"C:\Users\recla\zipcode-global\pages"

missing = []
for link in links:
    path = os.path.join(base_dir, link.replace('/', os.sep))
    if not os.path.exists(path):
        missing.append(link)

print("Missing files:", missing)
