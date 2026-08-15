import re
html = open(r'C:\Users\recla\zipcode-global\pages\usa\Mississippi\copiah.html', encoding='utf-8').read()
matches = re.findall(r'<a[^>]+href=[\'"](/[^"\'\n]+)[\'"][^>]*>', html)
for m in matches[:5]:
    print(m)
