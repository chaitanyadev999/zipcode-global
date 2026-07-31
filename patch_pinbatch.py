import re
import os

files = [
    r'C:\Users\recla\zipcode-global\generate_pages.py',
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html'
]

old_code = r"const off = val\(r, 'officename'\) \|\| val\(r, 'office_name'\);\s*const place = off \? off : \(val\(r,f\.city\)\|\|val\(r,f\.dist\)\|\|''\);\s*const meta = off \? \(val\(r,f\.city\)\|\|val\(r,f\.dist\)\|\|''\) : \(val\(r,f\.dist\)\|\|val\(r,f\.state\)\|\|''\);"

new_code = """const off = val(r, 'officename') || val(r, 'office_name');
      let realCity = '';
      if (C.code === 'IN' && off) {
         realCity = String(off).replace(/ (B\\.O|S\\.O|H\\.O|V\\.O|Branch Office|Sub Office|Head Office)/ig, '').trim();
         realCity = realCity.replace(/[\\-,]+$/, '').trim();
      }
      
      let place = off ? off : (val(r,f.city)||val(r,f.dist)||'');
      let meta = off ? (val(r,f.city)||val(r,f.dist)||'') : (val(r,f.dist)||val(r,f.state)||'');

      if (C.code === 'IN' && realCity && realCity !== off) {
          place = realCity;
          meta = off;
      }"""

for file_path in files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(old_code, new_code, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {file_path}")

