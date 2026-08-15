import re

path = r'C:\Users\recla\zipcode-global\pages\shared_pseo.css'
with open(path, 'r', encoding='utf-8') as f:
    css = f.read()

nav_css = """
/* ── NAV OVERRIDE (from main.html) ── */
.nav {
  position:fixed;top:0;left:0;right:0;z-index:9999;
  padding:.9rem 2rem;display:flex;align-items:center;justify-content:space-between;
  transition:all .3s var(--ease);
  background: var(--bg-base);
}
.nav.scrolled {
  background:rgba(5,8,22,0.88);backdrop-filter:blur(24px);
  border-bottom:1px solid var(--border);
}
.nav-brand {display:flex;align-items:center;gap:.7rem;font-family:var(--font-display);font-weight:700;font-size:1.08rem; color: #fff;}
.nav-brand img {width:36px;height:36px;border-radius:9px;background:var(--grad-saffron);box-shadow:0 0 20px rgba(0,212,255,0.4); object-fit:cover;}
.nav-links {display:flex;align-items:center;gap:.5rem;}
.nav-btn {
  padding:.4rem .9rem;border-radius:999px;font-size:.8rem;font-weight:600;
  background:var(--bg-glass);border:1px solid var(--border);color:var(--text-2);
  transition:all .25s var(--ease); text-decoration: none;
}
.nav-btn:hover {background:var(--bg-card-hi);border-color:var(--saffron);color:var(--text);transform:translateY(-1px);}

@media(max-width:768px) {
  .nav {flex-direction:column; gap:0.8rem; padding:0.8rem 1.25rem;}
  .nav-links {overflow-x:auto; width:100%; padding-bottom:0.5rem; justify-content:flex-start; -ms-overflow-style:none; scrollbar-width:none;}
  .nav-links::-webkit-scrollbar { display: none; }
}
"""

if '.nav {' not in css:
    css += nav_css

with open(path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update shared_pseo.js to add buttons and fix nav scroll
js_path = r'C:\Users\recla\zipcode-global\pages\shared_pseo.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Add scroll listener for .nav
scroll_js = """
window.addEventListener('scroll', () => {
  const nav = document.querySelector('.nav');
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 40);
}, {passive:true});
"""
if "nav.classList.toggle('scrolled'" not in js:
    js = js.replace('// Initialization', scroll_js + '\n// Initialization')

# 2. Add buttons to results render
buttons_js = """
      if (chunkIndex < results.length) {
        requestAnimationFrame(renderChunk);
      } else {
        const moreHtml = `
          <div style="margin-top: 2rem; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;">
            <a href="/pages/${COUNTRY.flagCode}.html" class="action-btn" style="background: linear-gradient(135deg, #ff6b1a 0%, #f5b700 100%); color: #000; padding: 0.8rem 1.5rem; font-weight: bold; border-radius: 8px; text-decoration: none;">🔍 Find More Pincodes in ${COUNTRY.name}</a>
            <a href="https://www.google.com/search?q=${encodeURIComponent(title + ' postal code')}" target="_blank" class="action-btn" style="background: #333; color: #fff; padding: 0.8rem 1.5rem; font-weight: bold; border-radius: 8px; text-decoration: none;">🌍 Google Search</a>
          </div>
        `;
        resultsList.insertAdjacentHTML('beforeend', moreHtml);
      }
"""
js = js.replace('if (chunkIndex < results.length) {\n        requestAnimationFrame(renderChunk);\n      }', buttons_js)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
