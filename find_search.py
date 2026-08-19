with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'id=\"searchInput\"', text)
for m in matches:
    print(text[m.start()-100:m.end()+100])
