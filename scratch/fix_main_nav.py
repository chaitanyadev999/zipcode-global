import os

filepath = os.path.join(os.getcwd(), 'home', 'main.html')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix logo link
content = content.replace('<a class="brand" href="/home/main.html">', '<a class="brand" href="/">')

# Fix nav button
content = content.replace('<a class="nav-btn primary" href="/pages/india.html">🇮🇳 India PIN</a>', '<a class="nav-btn primary" href="/#countriesSection">🌍 All Countries</a>')

# Fix footer links
old_footer = """    <a href="/pages/india.html">India PIN Codes</a>
    <a href="/pages/usa.html">USA ZIP Codes</a>
    <a href="/pages/gb.html">UK Postcodes</a>
    <a href="/pages/au.html">Australia Postcodes</a>
    <a href="/pages/about.html">About</a>
    <a href="/pages/privacy.html">Privacy</a>"""

new_footer = """    <a href="/#countriesSection">🌍 All Countries</a>
    <a href="/pages/about.html">About</a>
    <a href="/pages/privacy.html">Privacy Policy</a>
    <a href="/pages/report.html">Report Issue</a>"""

content = content.replace(old_footer, new_footer)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("main.html updated.")
