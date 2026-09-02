
import os, glob, re

def patch_ad_slots(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        encoding = "utf-8"
    except UnicodeDecodeError:
        with open(filepath, "r", encoding="utf-16") as f:
            content = f.read()
        encoding = "utf-16"
        
    original = content
    
    if ".ad-slot:not(:has(> *))" not in content:
        ad_css = """
  /* Responsive UI Fixes */
  .ad-slot:not(:has(> *)), .ad-slot-container:not(:has(> *)), .ad-slot:empty, .ad-slot-container:empty { 
    display: none !important; margin: 0 !important; min-height: 0 !important; padding: 0 !important; border: none !important; 
  }
"""
        content = content.replace("</style>", ad_css + "</style>", 1)

    if content != original:
        with open(filepath, "w", encoding=encoding) as f:
            f.write(content)

for f in glob.glob("*.html") + glob.glob("pages/*.html"):
    patch_ad_slots(f)

# Fix index.html search box
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

if "@media(max-width:768px){\n    .search-box" not in index_content:
    search_css_fix = """
  @media(max-width:768px){
    .search-box { flex-direction: column; border-radius: 12px; padding: 1rem; align-items: stretch; gap: 0.5rem; }
    .search-box select { width: 100%; border-right: none; border-bottom: 1px solid rgba(0,212,255,0.3); padding-bottom: 0.5rem; text-align: center; }
    .search-box input { width: 100%; padding: 0.5rem 0; text-align: center; }
    .search-box button { width: 100%; }
  }
"""
    index_content = index_content.replace("</style>", search_css_fix + "</style>", 1)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_content)

print("Applied responsive UI fixes!")
