import os

template_file = r'C:\Users\recla\zipcode-global\pages\country-template.html'

with open(template_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('href="/p/about.html"', 'href="/pages/about.html"')
content = content.replace('href="/p/privacy.html"', 'href="/pages/privacy.html"')
content = content.replace('href="/p/report.html"', 'href="/pages/report.html"')

with open(template_file, 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Fixed /p/ links to /pages/ in country-template.html")
