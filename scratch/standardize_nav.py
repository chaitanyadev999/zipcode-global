import os
import re

NAV_TEMPLATE = """<nav class="nav" id="mainNav">
  <a class="brand" href="{home_path}">
    <div class="brand-icon"><img src="{home_dir}assets/logo.png" alt="PO ZipCode Global Logo" loading="lazy"></div>
    <span>PO ZipCode Global</span>
  </a>
  <div class="nav-links">
    <a class="nav-btn" href="{home_path}">🏠 Home Page</a>
    <a class="nav-btn" style="color:var(--p); border-color:var(--p)" href="{pages_dir}translate.html">Translator</a>
    <a class="nav-btn" href="{pages_dir}blog.html">Blog</a>
    <a class="nav-btn" href="{pages_dir}about.html">About</a>
    <a class="nav-btn" href="{pages_dir}privacy.html">Privacy</a>
    <a class="nav-btn" href="{pages_dir}report.html">Report</a>
    <div id="google_translate_element"></div>
  </div>
</nav>"""

base_dir = r'C:\Users\recla\zipcode-global'
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            depth = len(os.path.relpath(filepath, base_dir).split(os.sep)) - 1
            if depth == 0:
                # Root level
                home_path = 'home/main.html'
                home_dir = 'home/'
                pages_dir = 'pages/'
            elif root.endswith('home'):
                # In home/
                home_path = 'main.html'
                home_dir = ''
                pages_dir = '../pages/'
            elif root.endswith('pages'):
                # In pages/
                home_path = '../home/main.html'
                home_dir = '../home/'
                pages_dir = ''
            else:
                # Deeper (e.g., pages/blog/, pages/india/)
                home_path = '../../home/main.html'
                home_dir = '../../home/'
                pages_dir = '../'
            
            nav_html = NAV_TEMPLATE.format(home_path=home_path, home_dir=home_dir, pages_dir=pages_dir)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace nav
            if '<nav class="nav" id="mainNav">' in content:
                content = re.sub(r'<nav class="nav" id="mainNav">.*?</nav>', nav_html, content, flags=re.DOTALL)
            elif '<nav class="country-nav"' in content:
                content = re.sub(r'<nav class="country-nav".*?</nav>', nav_html, content, flags=re.DOTALL)
            elif '<nav ' in content:
                content = re.sub(r'<nav .*?</nav>', nav_html, content, flags=re.DOTALL)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Standardized navigation across all HTML files.")
