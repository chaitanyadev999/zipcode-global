import os
import re

NAV_HTML = """<nav class="nav" id="mainNav">
  <a class="brand" href="../home/main.html">
    <div class="brand-icon"><img src="../home/assets/logo.png" alt="PO ZipCode Global Logo" loading="lazy"></div>
    <span>PO ZipCode Global</span>
  </a>
  <div class="nav-links">
    <a class="nav-btn" href="../home/main.html">🏠 Home Page</a>
    <a class="nav-btn" style="color:var(--p); border-color:var(--p)" href="translate.html">Translator</a>
    <a class="nav-btn" href="blog.html">Blog</a>
    <a class="nav-btn" href="about.html">About</a>
    <a class="nav-btn" href="privacy.html">Privacy</a>
    <a class="nav-btn" href="report.html">Report</a>
    <div id="google_translate_element"></div>
  </div>
</nav>"""

file_path = r'C:\Users\recla\zipcode-global\pages\country-template.html'
html = open(file_path, encoding='utf-8').read()

html = re.sub(r'<nav class="country-nav".*?</nav>', NAV_HTML, html, flags=re.DOTALL)
html = re.sub(r'<style>.*?</style>', lambda m: m.group(0).replace('.country-nav', '.nav'), html, flags=re.DOTALL)

open(file_path, 'w', encoding='utf-8').write(html)
print("Updated country-template.html")
