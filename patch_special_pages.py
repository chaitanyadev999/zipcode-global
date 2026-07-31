import re
import os

files = [
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html'
]

old_labels = """      if(low === 'circlename') label = 'Circle Name';
      if(low === 'regionname') label = 'Region Name';
      if(low === 'divisionname') label = 'Division Name';
      if(low === 'officename') label = 'Office Name';"""

new_labels = """      if(low === 'circlename') label = 'Circle';
      if(low === 'regionname') label = 'Region';
      if(low === 'divisionname') label = 'City';
      if(low === 'officename') label = 'Post Office';"""

old_code = """      const pin = val(r,f.pin)||'—';
      const place = val(r,f.city)||val(r,f.dist)||'';
      const meta = val(r,f.dist)||val(r,f.state)||'';"""

new_code = """      const pin = val(r,f.pin)||'—';
      const off = val(r, 'officename') || val(r, 'office_name');
      const place = off ? off : (val(r,f.city)||val(r,f.dist)||'');
      const meta = off ? (val(r,f.city)||val(r,f.dist)||'') : (val(r,f.dist)||val(r,f.state)||'');"""

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace(old_labels, new_labels)
        content = content.replace(old_code, new_code)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")

