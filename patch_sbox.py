
import glob

def patch_sbox(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        encoding = "utf-8"
    except UnicodeDecodeError:
        with open(filepath, "r", encoding="utf-16") as f:
            content = f.read()
        encoding = "utf-16"
        
    if "@media(max-width:768px){\n    .sbox" not in content and ".sbox{" in content:
        sbox_css = """
  @media(max-width:768px){
    .sbox { flex-direction: column; border-radius: 12px; padding: 0.8rem; background: rgba(8,12,32,1); }
    .sbox input { width: 100%; text-align: center; }
    .sbtn { width: 100%; }
  }
"""
        content = content.replace("</style>", sbox_css + "</style>", 1)
        with open(filepath, "w", encoding=encoding) as f:
            f.write(content)

for f in glob.glob("pages/*.html"):
    patch_sbox(f)

print("sbox patched for mobile!")
