import re
import os

files = [
    r'C:\Users\recla\zipcode-global\home\main.html',
    r'C:\Users\recla\zipcode-global\pages\about.html',
    r'C:\Users\recla\zipcode-global\pages\privacy.html',
    r'C:\Users\recla\zipcode-global\pages\report.html'
]

for file_path in files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add --p, --a, --p2 to the root block if they are missing
    if '--p:' not in content:
        content = content.replace(
            ':root {', 
            ':root {\n              --p: #00d4ff;\n              --a: #7c3aed;\n              --p2: 0,212,255;\n              --p2-rgb: 0,212,255;'
        ).replace(
            ':root{', 
            ':root{\n    --p: #00d4ff;\n    --a: #7c3aed;\n    --p2: 0,212,255;\n    --p2-rgb: 0,212,255;'
        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {file_path}")

