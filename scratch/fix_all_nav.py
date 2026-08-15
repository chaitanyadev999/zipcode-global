import os

pages_dir = r'C:\Users\recla\zipcode-global\pages'
html_files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

for f in html_files:
    path = os.path.join(pages_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    orig = content
    
    # Fix brand link
    content = content.replace('<a class="brand" href="/home/main.html">', '<a class="brand" href="../home/main.html">')
    
    # Fix nav links (make them relative since we are already inside pages/)
    content = content.replace('href="/home/main.html"', 'href="../home/main.html"')
    content = content.replace('href="/pages/translate.html"', 'href="translate.html"')
    content = content.replace('href="/pages/blog.html"', 'href="blog.html"')
    content = content.replace('href="/pages/about.html"', 'href="about.html"')
    content = content.replace('href="/pages/privacy.html"', 'href="privacy.html"')
    content = content.replace('href="/pages/report.html"', 'href="report.html"')
    
    # Remove any duplicates of Home Page that might have accumulated
    # We want exactly ONE Home page link in nav-links
    # Let's clean the nav-links block completely and rebuild it to guarantee consistency
    if '<div class="nav-links">' in content:
        # Extract everything before and after nav-links
        pre = content.split('<div class="nav-links">')[0]
        post = content.split('<div class="nav-links">')[1]
        
        # Find the end of nav-links
        end_idx = post.find('</nav>')
        after_nav = post[end_idx:]
        
        # Build the perfect consistent nav block for pages/
        perfect_nav = """<div class="nav-links">
    <a class="nav-btn" href="../home/main.html">🏠 Home Page</a>
    <a class="nav-btn" style="color:var(--p); border-color:var(--p)" href="translate.html">Translator</a>
    <a class="nav-btn" href="blog.html">Blog</a>
    <a class="nav-btn" href="about.html">About</a>
    <a class="nav-btn" href="privacy.html">Privacy</a>
    <a class="nav-btn" href="report.html">Report</a>
    <div id="google_translate_element"></div>
  </div>
"""
        content = pre + perfect_nav + after_nav
    
    if orig != content:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

# Fix main.html (which is in home/)
main_path = r'C:\Users\recla\zipcode-global\home\main.html'
with open(main_path, 'r', encoding='utf-8') as file:
    content = file.read()

orig = content
content = content.replace('<a class="brand" href="/">', '<a class="brand" href="main.html">')

if '<div class="nav-links">' in content:
    pre = content.split('<div class="nav-links">')[0]
    post = content.split('<div class="nav-links">')[1]
    end_idx = post.find('</nav>')
    after_nav = post[end_idx:]
    
    perfect_nav = """<div class="nav-links">
    <a class="nav-btn" href="main.html">🏠 Home Page</a>
    <a class="nav-btn" style="color:var(--p); border-color:var(--p)" href="../pages/translate.html">Translator</a>
    <a class="nav-btn" href="../pages/blog.html">Blog</a>
    <a class="nav-btn" href="../pages/about.html">About</a>
    <a class="nav-btn" href="../pages/privacy.html">Privacy</a>
    <a class="nav-btn" href="../pages/report.html">Report</a>
    <div id="google_translate_element"></div>
  </div>
"""
    content = pre + perfect_nav + after_nav

if orig != content:
    with open(main_path, 'w', encoding='utf-8') as file:
        file.write(content)
