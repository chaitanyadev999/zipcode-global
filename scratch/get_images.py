import glob
import re

files = glob.glob(r'C:\Users\recla\zipcode-global\pages\blog\*.html')
for f in files:
    content = open(f, 'r', encoding='utf-8').read()
    match = re.search(r'<img[^>]+src="([^"]+)"', content)
    if match:
        print(f.split('\\')[-1], match.group(1))
