import re
import os

files = [
    r'C:\Users\recla\zipcode-global\generate_pages.py',
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html',
    r'C:\Users\recla\zipcode-global\pages\country-template.html'
]

css_patch = """.hero-bg{position:absolute;top:0;left:0;width:100%;height:600px;background-size:cover;background-position:center;opacity:0.15;z-index:-1;mask-image:linear-gradient(to bottom, black 0%, transparent 100%);-webkit-mask-image:linear-gradient(to bottom, black 0%, transparent 100%);pointer-events:none}
  .hero{"""

def patch_file(fpath):
    if not os.path.exists(fpath): return
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS
    if '.hero-bg{' not in content:
        content = content.replace('.hero{', css_patch, 1)

    # 2. Add HTML
    if '<div class="hero-bg"' not in content:
        if 'generate_pages.py' in fpath:
            content = content.replace('<section class="hero">', '<div class="hero-bg" style="background-image: url(\'https://flagcdn.com/w1280/{{CODE_LOWER}}.png\')"></div>\n  <section class="hero">')
        elif 'india.html' in fpath:
            content = content.replace('<section class="hero">', '<div class="hero-bg" style="background-image: url(\'https://flagcdn.com/w1280/in.png\')"></div>\n  <section class="hero">')
        elif 'usa.html' in fpath:
            content = content.replace('<section class="hero">', '<div class="hero-bg" style="background-image: url(\'https://flagcdn.com/w1280/us.png\')"></div>\n  <section class="hero">')
        elif 'country-template.html' in fpath:
            content = content.replace('<section class="hero">', '<div class="hero-bg" id="heroBg"></div>\n  <section class="hero">')
            # Also add JS for country-template
            if "heroBg" in content and "$('heroBg')" not in content:
                content = content.replace(
                    "$('heroFlag').innerHTML", 
                    "const hBg = document.getElementById('heroBg'); if(hBg) hBg.style.backgroundImage = `url('https://flagcdn.com/w1280/${COUNTRY.flagCode}.png')`;\n    $('heroFlag').innerHTML"
                )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {fpath}")

for f in files:
    patch_file(f)

