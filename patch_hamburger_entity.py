
import os, glob, re

def patch_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        encoding = "utf-8"
    except UnicodeDecodeError:
        with open(filepath, "r", encoding="utf-16") as f:
            content = f.read()
        encoding = "utf-16"
        
    original = content
    
    # Replace the literal ☰ with &#9776;
    content = content.replace(">☰</div>", ">&#9776;</div>")
    
    # Also fix font size if it was 1.8rem, reduce it slightly
    content = content.replace("font-size: 1.8rem;", "font-size: 1.5rem;")

    if content != original:
        with open(filepath, "w", encoding=encoding) as f:
            f.write(content)

for f in glob.glob("*.html") + glob.glob("pages/*.html"):
    patch_file(f)

print("Hamburger entity and size patched!")
