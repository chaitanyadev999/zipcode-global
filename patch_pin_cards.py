import re

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_code = """      const pin = val(r,f.pin)||'—';
      const place = val(r,f.city)||val(r,f.dist)||'';
      const meta = val(r,f.dist)||val(r,f.state)||'';"""

new_code = """      const pin = val(r,f.pin)||'—';
      const off = val(r, 'officename') || val(r, 'office_name');
      const place = off ? off : (val(r,f.city)||val(r,f.dist)||'');
      const meta = off ? (val(r,f.city)||val(r,f.dist)||'') : (val(r,f.dist)||val(r,f.state)||'');"""

content = content.replace(old_code, new_code)

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_pages.py renderPinBatch updated successfully!")
