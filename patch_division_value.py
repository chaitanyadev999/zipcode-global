import re
import os

files = [
    r'C:\Users\recla\zipcode-global\generate_pages.py',
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html'
]

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix showDetail to strip 'Division' from the value
        content = re.sub(
            r"if\(low === 'divisionname'\) label = 'City';",
            r"if(low === 'divisionname') { label = 'City'; if(typeof value === 'string') value = value.replace(/\\bDivision\\b/i, '').trim(); }",
            content
        )

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")

