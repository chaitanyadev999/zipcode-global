import re
html = open(r'C:\Users\recla\zipcode-global\home\main.html', encoding='utf-8').read()
matches = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
print("LINKS IN MAIN.HTML:")
for m in matches:
    print(m)
