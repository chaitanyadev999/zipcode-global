import re
import os

files = [
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html'
]

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix Labels
        content = re.sub(
            r"if\(low === 'circlename'\) label = 'Circle Name';\s*if\(low === 'regionname'\) label = 'Region Name';\s*if\(low === 'divisionname'\) label = 'Division Name';\s*if\(low === 'officename'\) label = 'Office Name';",
            """if(low === 'circlename') label = 'Circle';
      if(low === 'regionname') label = 'Region';
      if(low === 'divisionname') label = 'City';
      if(low === 'officename') label = 'Post Office';""",
            content
        )

        # Fix renderPinBatch
        content = re.sub(
            r"const pin = val\(r,f\.pin\)\|\|'—';\s*const place = val\(r,f\.city\)\|\|val\(r,f\.dist\)\|\|'';\s*const meta = val\(r,f\.dist\)\|\|val\(r,f\.state\)\|\|'';",
            """const pin = val(r,f.pin)||'—';
      const off = val(r, 'officename') || val(r, 'office_name');
      const place = off ? off : (val(r,f.city)||val(r,f.dist)||'');
      const meta = off ? (val(r,f.city)||val(r,f.dist)||'') : (val(r,f.dist)||val(r,f.state)||'');""",
            content
        )

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Regex Updated {file_path}")

