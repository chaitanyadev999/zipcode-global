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

pages = ['privacy.html', 'about.html', 'blog.html', 'report.html', 'translate.html']
base_dir = r'C:\Users\recla\zipcode-global\pages'

for page in pages:
    filepath = os.path.join(base_dir, page)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove the broken CSS I just added
    if '/* ── NAV ── */' in html and '<style id="navStyle">' not in html:
        # Find index of /* ── NAV ── */ and remove everything up to </head>
        idx = html.find('/* ── NAV ── */')
        head_end = html.find('</head>', idx)
        if idx != -1 and head_end != -1:
            html = html[:idx] + html[head_end:]

    # Remove the old navStyle if exists
    html = re.sub(r'<style id="navStyle">.*?</style>', '', html, flags=re.DOTALL)
    
    html = html.replace('</head>', standard_css + '\n</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Fixed {page}")

