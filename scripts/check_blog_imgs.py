import os
import re

d = r"C:\Users\recla\zipcode-global\pages\blog"
for f in os.listdir(d):
    path = os.path.join(d, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    images = re.findall(r'<img[^>]+src="([^"]+)"', content)
    print(f, images)
