import os
import re

filepath = r"C:\Users\recla\zipcode-global\pages\blog.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

posts = html.split('class="card"')
print("Total posts:", len(posts)-1)
for i, post in enumerate(posts):
    if i == 0: continue
    if '<img' not in post:
        print(f"Post {i} missing image!")
