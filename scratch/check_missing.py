import os, re
html = open(r'C:\Users\recla\zipcode-global\home\main.html', encoding='utf-8').read()
links = re.findall(r'href=[\'\"]([^\'\"]+)[\'\"]|src=[\'\"]([^\'\"]+)[\'\"]', html)
links = [l[0] or l[1] for l in links]
base = r'C:\Users\recla\zipcode-global\home'
missing = []
for l in links:
    if l.startswith(('http', 'mailto', 'tel', '#', 'javascript', 'data:')): continue
    l_clean = l.split('?')[0].split('#')[0]
    full_path = os.path.normpath(os.path.join(base, l_clean))
    if not os.path.exists(full_path):
        missing.append(l)
print(f"Missing files: {missing}")
