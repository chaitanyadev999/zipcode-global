import re
import os

files = [
    r'C:\Users\recla\zipcode-global\generate_pages.py',
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html'
]

old_regex = r"let realCity = String\(r\['officename'\]\)\.replace\(/ \(B\\\.O\|S\\\.O\|H\\\.O\|V\\\.O\|Branch Office\|Sub Office\|Head Office\) /ig, ''\)\.trim\(\);"
new_regex = r"let realCity = String(r['officename']).replace(/ (B\.O|S\.O|H\.O|V\.O|Branch Office|Sub Office|Head Office)/ig, '').trim();"

old_html = r"\$\('diGrid'\)\.innerHTML = realCityHtml \+ itemsHtml;"
new_html = r"$('diGrid').innerHTML = realCityHtml + itemsHtml + (C.code==='IN' ? `<div style='grid-column: 1 / -1; font-size:0.85rem; color:#888; background:rgba(255,255,255,0.03); padding:8px 12px; border-radius:6px; margin-top:5px;'><b>💡 Abbreviations:</b> B.O = Branch Office, S.O = Sub Office, H.O = Head Office, V.O = Village Office</div>` : '');"


for file_path in files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_regex in content:
        content = content.replace(
            "let realCity = String(r['officename']).replace(/ (B\\.O|S\\.O|H\\.O|V\\.O|Branch Office|Sub Office|Head Office) /ig, '').trim();",
            "let realCity = String(r['officename']).replace(/ (B\\.O|S\\.O|H\\.O|V\\.O|Branch Office|Sub Office|Head Office)/ig, '').trim();"
        )
    
    if "$('diGrid').innerHTML = realCityHtml + itemsHtml;" in content:
        content = content.replace(
            "$('diGrid').innerHTML = realCityHtml + itemsHtml;",
            new_html
        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {file_path}")

