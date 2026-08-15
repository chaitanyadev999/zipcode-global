import os
import re

filepath = r"C:\Users\recla\zipcode-global\pages\blog\canadian-postal-codes.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

images = re.findall(r'<img[^>]+src="([^"]+)"', html)
for img in images:
    print(img)
