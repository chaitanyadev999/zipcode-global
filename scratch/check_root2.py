import re
html = open(r'C:\Users\recla\zipcode-global\pages\country-template.html', encoding='utf-8').read()
matches = re.findall(r'href=[\'"](/[^"\'\n]+)[\'"]', html)
for m in set(matches):
    print(m)
