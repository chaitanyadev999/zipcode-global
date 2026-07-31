import re
import os

file_path = r'C:\Users\recla\zipcode-global\home\main.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Slow down the marquee animation
content = content.replace('animation: scrollX 150s linear', 'animation: scrollX 350s linear')

# Remove Pakistan from footer
content = re.sub(r'<a href="/pages/pk\.html">Pakistan Postal</a>\s*', '', content)

# Remove Pakistan from JS countries array
content = re.sub(r"\{code:'PK',name:'Pakistan'.*?\},?\s*", '', content)

# Extra slow down for the dynamically generated JS marquee speed if there is one
content = content.replace('const duration = 240 + (r % 3)*60;', 'const duration = 400 + (r % 3)*100;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched main.html successfully.")
