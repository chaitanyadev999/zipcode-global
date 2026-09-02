
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

    if "<div class=\"hamburger\"" not in content:
        content = content.replace(
            "<div class=\"nav-links\">",
            "<div class=\"hamburger\" onclick=\"document.querySelector(\x27.nav-links\x27).classList.toggle(\x27active\x27)\">☰</div>\n    <div class=\"nav-links\">"
        )

    if ".hamburger {" not in content:
        hamburger_css = """
  .hamburger { display: none; font-size: 1.8rem; cursor: pointer; color: var(--t); user-select: none; line-height: 1; margin-left: auto; }
  @media(max-width:768px){
    .nav { flex-direction: row !important; align-items: center !important; padding: 0.8rem 1.25rem !important; }
    .hamburger { display: block; }
    .nav-links {
      display: none !important; position: absolute; top: 100%; left: 0; width: 100%;
      background: rgba(5, 8, 22, 0.98); backdrop-filter: blur(15px);
      flex-direction: column !important; padding: 1.5rem !important; 
      border-bottom: 1px solid rgba(0, 212, 255, 0.2);
      gap: 1rem !important; align-items: stretch !important; z-index: 10000;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .nav-links.active { display: flex !important; }
    .nav-btn { text-align: center; padding: 0.8rem; }
    #google_translate_element { text-align: center; margin: 10px auto !important; }
  }
"""
        content = content.replace("</style>", hamburger_css + "</style>")

    if content != original:
        with open(filepath, "w", encoding=encoding) as f:
            f.write(content)

for f in glob.glob("*.html"):
    patch_file(f)

for f in glob.glob("pages/*.html"):
    patch_file(f)

print("Hamburger patch applied to all files!")
