import os
import re

files = ["about.html", "privacy.html", "report.html", "blog.html"]

for f in files:
    path = os.path.join("C:/Users/recla/zipcode-global/pages", f)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Add translator link back
        if "translate.html" not in content:
            content = content.replace('<div class="nav-links">', '<div class="nav-links">\n      <a class="nav-btn" style="color:var(--p); border-color:var(--p)" href="/pages/translate.html">Translator</a>')
            
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Patched {f}")
