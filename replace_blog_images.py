import os
import re
import random

# Replace images in blog.html
blog_html_path = r"C:\Users\recla\zipcode-global\pages\blog.html"
with open(blog_html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any https://images.unsplash.com/... with /home/assets/blog/cover1.png, cover2.png, cover3.png in a cycle
unsplash_urls = list(set(re.findall(r'https://images.unsplash.com/[^"]+', html)))
cover_images = ['/home/assets/blog/cover1.png', '/home/assets/blog/cover2.png', '/home/assets/blog/cover3.png']
mapping = {}
for i, url in enumerate(unsplash_urls):
    mapping[url] = cover_images[i % 3]

for url, local_img in mapping.items():
    html = html.replace(url, local_img)

with open(blog_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated blog.html")

# Replace images in the individual blog posts
blog_dir = r"C:\Users\recla\zipcode-global\pages\blog"
for f in os.listdir(blog_dir):
    if f.endswith('.html'):
        filepath = os.path.join(blog_dir, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        modified = False
        for url, local_img in mapping.items():
            if url in content:
                content = content.replace(url, local_img)
                modified = True
                
        # If it doesn't have an unsplash URL but we still want to make sure it has a cover image
        if modified:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated {f}")

