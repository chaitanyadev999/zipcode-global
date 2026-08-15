import os

pages = ['privacy.html', 'about.html', 'blog.html', 'report.html', 'translate.html']
base_dir = r'C:\Users\recla\zipcode-global\pages'

new_nav = """<nav class="cinema-nav">
  <div class="container" style="display:flex; justify-content:space-between; align-items:center;">
    <a class="brand" href="/home/main.html">
      <div class="brand-icon"><img src="/home/assets/logo.png" alt="PO ZipCode Global Logo"></div>
      <span>PO ZipCode Global</span>
    </a>
    <div class="nav-links">
      <a class="nav-btn" style="color:var(--p); border-color:var(--p)" href="/pages/translate.html">Translator</a>
      <a class="nav-btn" href="/pages/blog.html">Blog</a>
      <a class="nav-btn" href="/pages/about.html">About</a>
      <a class="nav-btn" href="/pages/privacy.html">Privacy</a>
      <a class="nav-btn" href="/pages/report.html">Report</a>
      <div id="google_translate_element"></div>
      <a class="nav-btn primary" href="/home/main.html#countriesSection">🌍 All Countries</a>
    </div>
  </div>
</nav>"""

for page in pages:
    filepath = os.path.join(base_dir, page)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    start_idx = html.find('<nav')
    end_idx = html.find('</nav>')
    
    if start_idx != -1 and end_idx != -1:
        # replace everything from <nav ...> to </nav>
        html = html[:start_idx] + new_nav + html[end_idx+6:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Updated {page}')
