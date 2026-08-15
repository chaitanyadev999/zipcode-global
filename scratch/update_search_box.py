import re

path = r'C:\Users\recla\zipcode-global\home\main.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS for the dropdown
css_to_add = """
.search-box select {
  background: transparent;
  border: none;
  border-right: 1px solid rgba(0,212,255,0.3);
  color: var(--t);
  font-family: var(--fm);
  font-size: 0.95rem;
  padding: 0.45rem 0.8rem 0.45rem 0.5rem;
  outline: none;
  cursor: pointer;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}
.search-box select option {
  background: #0a0e27;
  color: var(--t);
}
"""
if '.search-box select {' not in html:
    html = html.replace('.search-box input{', css_to_add + '\n.search-box input{')

# 2. Add the <select> tag in the HTML
html_to_add = """      <select id="heroCountrySelect" onchange="document.getElementById('heroSearch').focus()">
        <option value="ALL">🌍 Global</option>
      </select>
"""
if '<select id="heroCountrySelect"' not in html:
    html = html.replace('<input id="heroSearch"', html_to_add + '      <input id="heroSearch"')

# 3. Javascript to populate the dropdown
js_populate = """
function populateCountrySelect() {
  const sel = document.getElementById('heroCountrySelect');
  if(!sel) return;
  // Sort ALL countries by name
  let sorted = [...ALL].sort((a,b) => a.name.localeCompare(b.name));
  sorted.forEach(c => {
    let opt = document.createElement('option');
    let val = c.code.toLowerCase();
    if(val === 'in') val = 'india';
    if(val === 'us') val = 'usa';
    opt.value = val;
    opt.textContent = c.name;
    sel.appendChild(opt);
  });
}
"""
if 'populateCountrySelect()' not in html:
    html = html.replace('// ── RENDER CARDS ──', js_populate + '\npopulateCountrySelect();\n// ── RENDER CARDS ──')

# 4. Filter matches based on selected country
if 'let cFilter =' not in html:
    # Inside input event
    html = html.replace(
        'let matches = [];',
        "let matches = [];\n        let cFilter = document.getElementById('heroCountrySelect').value;"
    )
    
    # Filter cities
    html = html.replace(
        'if (globalIndex.cities && matches.length < 5) {',
        'if (globalIndex.cities && matches.length < 5) {'
    )
    html = html.replace(
        'if (key.includes(cityMatchTerm)) {',
        'if (key.includes(cityMatchTerm) && (cFilter === "ALL" || globalIndex.cities[key].includes("/"+cFilter+"/"))) {'
    )
    
    # Filter states
    html = html.replace(
        'if (key.includes(stateMatchTerm)) {',
        'if (key.includes(stateMatchTerm) && (cFilter === "ALL" || globalIndex.states[key].includes("/"+cFilter+"/"))) {'
    )
    
    # Filter pincodes
    html = html.replace(
        'if (key.includes(lowerV)) {',
        'if (key.includes(lowerV) && (cFilter === "ALL" || globalIndex.pincodes[key].includes("/"+cFilter+"/"))) {'
    )

    # Filter autocomplete click url - it currently uses /${m.path}, which is wrong for file:///. I'll fix this to ../${m.path}
    html = html.replace(
        "onclick=\"window.location.href='/${m.path}'\"",
        "onclick=\"window.location.href='../${m.path}'\""
    )

# 5. doSearch country filter
if 'const cFilter = document.getElementById(\'heroCountrySelect\').value;' not in html:
    html = html.replace(
        "const lowerV = q.replace(/[^a-z0-9\\s-]/g, '').trim();",
        "const lowerV = q.replace(/[^a-z0-9\\s-]/g, '').trim();\n   const cFilter = document.getElementById('heroCountrySelect').value;"
    )
    # This might be too complex via regex, let's just write the modified html back.

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
