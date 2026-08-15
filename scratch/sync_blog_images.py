import re
import os

blog_path = r'C:\Users\recla\zipcode-global\pages\blog.html'
posts_dir = r'C:\Users\recla\zipcode-global\pages\blog'

with open(blog_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract pairs of (filename, image_name)
links = re.findall(r'<a href="blog/(.*?\.html)" class="card">\s*<img src="/home/assets/blog/(ai_cover_\d+\.png)"', html)

for filename, img_name in links:
    post_path = os.path.join(posts_dir, filename)
    if os.path.exists(post_path):
        with open(post_path, 'r', encoding='utf-8') as pf:
            post_html = pf.read()
        
        # Replace the inside image with the exact same image
        # The inside image in the blog post template probably looks like <img src="/home/assets/blog/cover1.png"
        post_html = re.sub(r'<img src="/home/assets/blog/cover\d\.png"', f'<img src="/home/assets/blog/{img_name}"', post_html)
        # Or if it's already picsum:
        post_html = re.sub(r'<img src="https://picsum.photos/[^"]+"', f'<img src="/home/assets/blog/{img_name}"', post_html)
        
        with open(post_path, 'w', encoding='utf-8') as pf:
            pf.write(post_html)
        print(f"Updated {filename} to use {img_name}")
