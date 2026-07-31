import re
import os

files = [
    r'C:\Users\recla\zipcode-global\generate_pages.py',
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html'
]

for file_path in files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the .map-badge CSS block using regex
    content = re.sub(
        r"\.map-badge\{[^}]+\}",
        r".map-badge{\n    position:absolute;top:1rem;right:1rem;z-index:400;\n    max-width:calc(100% - 2rem);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;\n    padding:.4rem .9rem;border-radius:999px;background:rgba(5,8,22,0.85);\n    backdrop-filter:blur(16px);border:1px solid rgba(var(--p2),0.3);\n    font-family:var(--fm);font-size:.72rem;color:var(--p);box-shadow:0 4px 16px rgba(0,0,0,0.4);\n  }",
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {file_path}")

