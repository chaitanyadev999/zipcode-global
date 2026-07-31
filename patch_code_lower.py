import re
import os

files = [
    r'C:\Users\recla\zipcode-global\generate_pages.py'
]

for file_path in files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where {{CODE}} is replaced
    if 'content.replace("{{CODE_LOWER}}", c.code.lower())' not in content:
        content = content.replace(
            'content = content.replace("{{CODE}}", c.code)',
            'content = content.replace("{{CODE}}", c.code)\n        content = content.replace("{{CODE_LOWER}}", c.code.lower())'
        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {file_path}")

