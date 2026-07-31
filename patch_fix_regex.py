import re
import os

files = [
    r'C:\Users\recla\zipcode-global\generate_pages.py',
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html'
]

def patch_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update showDetail Place logic & realCity logic
    # Find the top of showDetail
    content = re.sub(
        r"const place = val\(r,f\.city\)\|\|val\(r,f\.dist\)\|\|val\(r,f\.state\)\|\|C\.name;",
        r"""let place = val(r,f.city)||val(r,f.dist)||val(r,f.state)||C.name;
    let realCity = '';
    if (C.code === 'IN' && r['officename']) {
        realCity = String(r['officename']).replace(/ (B\\.O|S\\.O|H\\.O|V\\.O|Branch Office|Sub Office|Head Office)/ig, '').trim();
        realCity = realCity.replace(/[\\-,]+$/, '').trim();
        if (realCity) place = realCity;
    }""",
        content
    )

    # 2. Update realCityHtml inside showDetail to use the already calculated realCity
    content = re.sub(
        r"let realCityHtml = '';\s*if \(C\.code === 'IN' && r\['officename'\]\) \{[^\}]+if \(realCity\) \{[^\}]+}[^\}]+}",
        r"""let realCityHtml = '';
    if (C.code === 'IN' && realCity) {
        realCityHtml = `<div class="di-item">
          <div class="di-item-lbl"><span>🏙️</span> City</div>
          <div class="di-item-val" style="color:var(--p);font-weight:600">${realCity}</div>
        </div>`;
    }""",
        content,
        flags=re.MULTILINE
    )
    
    # 3. Clean up the trailing space regex if it's still there
    content = re.sub(
        r"let realCity = String\(r\['officename'\]\)\.replace\(/ \(B\\\.O\|S\\\.O\|H\\\.O\|V\\\.O\|Branch Office\|Sub Office\|Head Office\) /ig, ''\)\.trim\(\);",
        r"let realCity = String(r['officename']).replace(/ (B\\.O|S\\.O|H\\.O|V\\.O|Branch Office|Sub Office|Head Office)/ig, '').trim();",
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {file_path}")

for f in files:
    if os.path.exists(f):
        patch_file(f)

