import os
import re

standard_css = """
<style id="navStyle">
/* ── NAV ── */
.nav{
  position:fixed;top:0;left:0;right:0;z-index:9999;
  padding:.9rem 2rem;display:flex;align-items:center;justify-content:space-between;
  transition:all .3s var(--ease);
}
.nav.scrolled{
  background:rgba(5,8,22,0.88);backdrop-filter:blur(24px);
  border-bottom:1px solid var(--b);
}
.brand{display:flex;align-items:center;gap:.7rem;font-family:var(--fd);font-weight:700;font-size:1.08rem;color:#fff;text-decoration:none}
.brand-icon{
  width:36px;height:36px;border-radius:9px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;
  overflow:hidden;box-shadow:0 0 20px rgba(0,212,255,0.4);
}
.brand-icon img{width:100%;height:100%;object-fit:cover;border-radius:9px;}
.nav-links{display:flex;align-items:center;gap:.5rem}
.nav-btn{
  padding:.4rem .9rem;border-radius:999px;font-size:.8rem;font-weight:600;
  background:var(--glass);border:1px solid var(--b);color:var(--t2);text-decoration:none;
  transition:all .25s var(--ease);
}
.nav-btn:hover{background:var(--card-hi);border-color:var(--cyan);color:var(--t);transform:translateY(-1px)}
.nav-btn.primary{background:var(--grad);color:#000;border:none;box-shadow:0 4px 16px rgba(0,212,255,0.3)}
@media(max-width:768px){ .nav{padding:1rem;} .nav-links{display:none;} } 
</style>
"""

standard_nav_html = """<nav class="nav" id="mainNav">
  <a class="brand" href="/home/main.html">
    <div class="brand-icon"><img src="/home/assets/logo.png" alt="PO ZipCode Global Logo" loading="lazy"></div>
    <span>PO ZipCode Global</span>
  </a>
  <div class="nav-links">
    <a class="nav-btn" style="color:var(--cyan); border-color:var(--cyan)" href="/pages/translate.html">Translator</a>
    <a class="nav-btn" href="/pages/blog.html">Blog</a>
    <a class="nav-btn" href="/pages/about.html">About</a>
    <a class="nav-btn" href="/pages/privacy.html">Privacy</a>
    <a class="nav-btn" href="/pages/report.html">Report</a>
    <div id="google_translate_element"></div>
    <a class="nav-btn primary" href="/home/main.html#countriesSection">🌍 All Countries</a>
  </div>
</nav>"""

pages = ['privacy.html', 'about.html', 'blog.html', 'report.html', 'translate.html']
base_dir = r'C:\Users\recla\zipcode-global\pages'

for page in pages:
    filepath = os.path.join(base_dir, page)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove existing nav blocks
    nav_pattern = re.compile(r'<nav[^>]*>.*?</nav>', re.DOTALL)
    if nav_pattern.search(html):
        html = nav_pattern.sub(standard_nav_html, html)
            
    # Clean up old CSS conflicts that might interfere
    html = re.sub(r'\.nav\s*\{[^\}]+\}', '', html)
    html = re.sub(r'\.site-nav\s*\{[^\}]+\}', '', html)
    html = re.sub(r'\.nav-brand\s*\{[^\}]+\}', '', html)
    html = re.sub(r'\.nav-brand \.bmark\s*\{[^\}]+\}', '', html)
    html = re.sub(r'\.nav-brand \.bmark img\s*\{[^\}]+\}', '', html)
    html = re.sub(r'\.nav-links\s*\{[^\}]+\}', '', html)
    html = re.sub(r'\.nav-links a\s*\{[^\}]+\}', '', html)
    html = re.sub(r'\.nav-links a:hover\s*\{[^\}]+\}', '', html)
    html = re.sub(r'\.nav-links a\.active\s*\{[^\}]+\}', '', html)
    
    # Append the style to </head>
    html = html.replace('</head>', standard_css + '\n</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Standardized {page}")

