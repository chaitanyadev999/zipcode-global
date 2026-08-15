import os
import glob
import re

# Fix blog.html
blog_main = r'C:\Users\recla\zipcode-global\pages\blog.html'
content = open(blog_main, 'r', encoding='utf-8').read()
content = content.replace('src="/home/', 'src="../home/')
open(blog_main, 'w', encoding='utf-8').write(content)

# Map blog posts to their cover number based on the order in blog.html
# Let's extract the mapping from blog.html
mapping = {}
cards = re.findall(r'<a href="blog/([^"]+)".*?src="\.\./home/assets/blog/ai_cover_(\d+)\.png"', content, re.DOTALL)
for slug, num in cards:
    mapping[slug] = f'ai_cover_{num}.png'

blog_dir = r'C:\Users\recla\zipcode-global\pages\blog'
for html_file in glob.glob(os.path.join(blog_dir, '*.html')):
    slug = os.path.basename(html_file)
    if slug in mapping:
        img_name = mapping[slug]
        page_content = open(html_file, 'r', encoding='utf-8').read()
        
        # In the blog post html, the image might be /home/assets/logo.png or ../../home/assets/logo.png
        # Let's just find the first <img src="..."> in the <header> or <div class="hero"> or <article> and replace it
        # Actually it's probably <img src="/home/assets/logo.png"
        page_content = re.sub(r'src="[^"]+assets/logo\.png"', f'src="../../home/assets/blog/{img_name}"', page_content)
        page_content = re.sub(r'src="/home/assets/logo\.png"', f'src="../../home/assets/blog/{img_name}"', page_content)
        
        # Also fix the logo in the nav bar if it exists
        page_content = page_content.replace('src="/home/assets/logo.png"', 'src="../../home/assets/logo.png"')
        
        # Fix nav links if there are any /pages/
        page_content = page_content.replace('href="/pages/', 'href="https://zipcodeglobal.github.io/pages/')
        page_content = page_content.replace('href="/home/main.html"', 'href="../../home/main.html"')

        open(html_file, 'w', encoding='utf-8').write(page_content)

print("Fixed blog images and paths!")
