import os, glob

# 1. Fix stray ">" in link rel="icon"
for f in glob.glob("**/*.html", recursive=True):
    try:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
        enc = "utf-8"
    except:
        with open(f, "r", encoding="utf-16") as file:
            content = file.read()
        enc = "utf-16"
        
    original = content
    content = content.replace('<link rel="icon" type="image/png" href="/home/assets/logo.png"><text y=%22.9em%22 font-size=%2290%22>🌍</text></svg>">', '<link rel="icon" type="image/png" href="/home/assets/logo.png">')
    content = content.replace('<link rel="icon" type="image/png" href="../home/assets/logo.png"><text y=%22.9em%22 font-size=%2290%22>🌍</text></svg>">', '<link rel="icon" type="image/png" href="../home/assets/logo.png">')
    content = content.replace('<link rel="icon" type="image/png" href="home/assets/logo.png"><text y=%22.9em%22 font-size=%2290%22>🌍</text></svg>">', '<link rel="icon" type="image/png" href="home/assets/logo.png">')

    if content != original:
        with open(f, "w", encoding=enc) as file:
            file.write(content)
            
# 2. Fix home page hero stats alignment
try:
    with open("index.html", "r", encoding="utf-8") as f:
        idx_content = f.read()
    
    if ".hero-stats { gap: 0.8rem" not in idx_content:
        stats_patch = """
  @media(max-width:768px){
    .hero-stats { gap: 0.5rem; flex-wrap: nowrap; flex-direction: row; align-items: center; justify-content: center; overflow: hidden; width: 100%; padding: 0; margin-left: auto; margin-right: auto; }
    .stat-num { font-size: 1.15rem; display: block; }
    .stat-label { font-size: 0.6rem; letter-spacing: 0; }
    .stat-divider { margin: 0 0.2rem; height: 30px; }
    .stat-item { padding: 0; flex: 1; }
  }
"""
        idx_content = idx_content.replace("</style>", stats_patch + "</style>", 1)
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(idx_content)
except Exception as e:
    print(e)
    
# 3. Fix country-template.html search bar cut off
try:
    with open("pages/country-template.html", "r", encoding="utf-8") as f:
        tpl_content = f.read()
        
    if "/* Mobile Search Row Fix */" not in tpl_content:
        tpl_patch = """
  /* Mobile Search Row Fix */
  @media(max-width:768px){
    .search-row { flex-direction: column; background: transparent; border: none; padding: 0; }
    .search-row input { width: 100%; border-radius: var(--r-full); border: 1px solid var(--border); background: var(--bg-card); text-align: center; }
    .search-btn { width: 100%; border-radius: var(--r-full); }
    .voice-btn { position: absolute; right: 0.5rem; top: 0.35rem; width: 36px; height: 36px; font-size: 1rem; }
    .search-row { position: relative; display: flex; }
  }
"""
        tpl_content = tpl_content.replace("</style>", tpl_patch + "</style>", 1)
        with open("pages/country-template.html", "w", encoding="utf-8") as f:
            f.write(tpl_content)
except Exception as e:
    print(e)
    
# 4. Fix shared_pseo.js auto-scroll
try:
    with open("pages/shared_pseo.js", "r", encoding="utf-8") as f:
        js = f.read()
        
    # Add shouldScroll parameter
    js = js.replace("function searchAll(query) {", "function searchAll(query, shouldScroll=false) {")
    js = js.replace("setTimeout(() => $('resultsSection').scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);", "if(shouldScroll){setTimeout(() => $('resultsSection').scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);}")
    
    js = js.replace("searchBtnNode.addEventListener('click', () => searchAll(searchInputNode.value.trim()));", "searchBtnNode.addEventListener('click', () => searchAll(searchInputNode.value.trim(), true));")
    js = js.replace("searchInputNode.addEventListener('keypress', (e) => { if (e.key === 'Enter') searchBtnNode.click(); });", "searchInputNode.addEventListener('keypress', (e) => { if (e.key === 'Enter') searchAll(searchInputNode.value.trim(), true); });")
    
    # Voice search should also scroll
    js = js.replace("searchAll(transcript);", "searchAll(transcript, true);")
    
    # State pages local search auto-scroll fix
    js = js.replace("function performLocalSearch(query) {", "function performLocalSearch(query, shouldScroll=false) {")
    js = js.replace("setTimeout(() => $('resultsSection').scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);", "if(shouldScroll){setTimeout(() => $('resultsSection').scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);}")
    
    js = js.replace("$('searchBtn').addEventListener('click', () => performLocalSearch($('searchInput').value.trim()));", "$('searchBtn').addEventListener('click', () => performLocalSearch($('searchInput').value.trim(), true));")
    js = js.replace("$('searchInput').addEventListener('keypress', (e) => { if (e.key === 'Enter') $('searchBtn').click(); });", "$('searchInput').addEventListener('keypress', (e) => { if (e.key === 'Enter') performLocalSearch($('searchInput').value.trim(), true); });")

    with open("pages/shared_pseo.js", "w", encoding="utf-8") as f:
        f.write(js)
except Exception as e:
    print(e)
    
print("All patches applied!")
