import re
import os

files = [
    r'C:\Users\recla\zipcode-global\generate_pages.py',
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html'
]

for file_path in files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update s2 titles to say Divisions instead of Cities for IN
    content = re.sub(
        r"\$\('s1title'\)\.textContent = stLabel \+ ' — Cities';\s*setCount\('s1cnt', NAV\.distsList\.length, 'City'\);",
        r"$('s1title').textContent = stLabel + (C.code==='IN' ? ' — Divisions' : ' — Cities');\n      setCount('s1cnt', NAV.distsList.length, C.code==='IN'?'Division':'City');",
        content
    )
    content = re.sub(
        r"\$\('s2title'\)\.textContent = dist \+ ' — Cities';\s*setCount\('s2cnt', NAV\.citiesList\.length, 'City'\);",
        r"$('s2title').textContent = dist + (C.code==='IN' ? ' — Divisions' : ' — Cities');\n    setCount('s2cnt', NAV.citiesList.length, C.code==='IN'?'Division':'City');",
        content
    )

    # 2. Update showDetail Labels to correctly map division to Division, and insert a synthetic REAL CITY for IN
    old_labels_regex = r"if\(low === 'circlename'\) label = 'Circle';\s*if\(low === 'regionname'\) label = 'Region';\s*if\(low === 'divisionname'\) \{ label = 'City'; if\(typeof value === 'string'\) value = value\.replace\(/\\bDivision\\b/i, ''\)\.trim\(\); \}\s*if\(low === 'officename'\) label = 'Post Office';"
    
    # In case the regex above fails (if the file doesn't have it exactly), provide a fallback pattern
    old_labels_fallback = r"if\(low === 'circlename'\) label = 'Circle Name';\s*if\(low === 'regionname'\) label = 'Region Name';\s*if\(low === 'divisionname'\) label = 'Division Name';\s*if\(low === 'officename'\) label = 'Office Name';"
    
    new_labels = """if(low === 'circlename') label = 'Circle';
      if(low === 'regionname') label = 'Region';
      if(low === 'divisionname') { label = 'Division'; if(typeof value === 'string') value = value.replace(/\\bDivision\\b/i, '').trim(); }
      if(low === 'officename') label = 'Post Office';"""
      
    if re.search(old_labels_regex, content):
        content = re.sub(old_labels_regex, new_labels, content)
    else:
        content = re.sub(old_labels_fallback, new_labels, content)

    # 3. Add the synthetic Real City field into the rendered itemsHtml in showDetail
    # We will inject it right before `$('diGrid').innerHTML = itemsHtml;`
    inject_point = r"\$\('diGrid'\)\.innerHTML = itemsHtml;"
    
    real_city_code = """
    let realCityHtml = '';
    if (C.code === 'IN' && r['officename']) {
        let realCity = String(r['officename']).replace(/\\b(B\\.O|S\\.O|H\\.O|V\\.O|Branch Office|Sub Office|Head Office)\\b/ig, '').trim();
        // Remove trailing hyphens or commas
        realCity = realCity.replace(/[\\-,]+$/, '').trim();
        if (realCity) {
            realCityHtml = `<div class="di-item">
              <div class="di-item-lbl"><span>🏙️</span> City</div>
              <div class="di-item-val" style="color:var(--p);font-weight:600">${realCity}</div>
            </div>`;
        }
    }
    
    $('diGrid').innerHTML = realCityHtml + itemsHtml;"""
    
    if "realCityHtml =" not in content:
        content = re.sub(inject_point, real_city_code, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {file_path}")

