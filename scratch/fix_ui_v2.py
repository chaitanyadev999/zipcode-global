import os
import re

pages_dir = r'C:\Users\recla\zipcode-global\pages'
html_files = [f for f in os.listdir(pages_dir) if f.endswith('.html') and not f.startswith('shared')]
html_files.append('layout.html')
fixed_count = 0

for f in html_files:
    path = os.path.join(pages_dir, f)
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    orig = content

    content = content.replace('<a class="nav-btn primary" href="/home/main.html">🏠 Home Page</a>', '')
    content = content.replace('<a class="nav-btn" href="/home/main.html">🏠 Home Page</a>', '')
    content = content.replace('<a class="nav-btn primary" href="/home/main.html#countriesSection">🌍 All Countries</a>', '')
    if '<div class="nav-links">' in content:
        content = content.replace('<div class="nav-links">', '<div class="nav-links">\n    <a class="nav-btn" href="/home/main.html">🏠 Home Page</a>', 1)

    show_detail_pattern = re.compile(r'function\s+showDetail\s*\(\s*i\s*\)\s*\{.*?document\.getElementById\(\'detailModal\'\)\.style\.display\s*=\s*\'flex\';\s*\}', re.DOTALL)
    dynamic_show_detail = """function showDetail(i) {
      const p = NAV.data[i];
      if(!p) return;
      document.getElementById('modalTitle').innerText = (p.pincode || p.zip || p.postal_code || '') + ' - ' + (p.officename || p.place_name || p.city || p.village || 'Details');
      let html = '<table class="info-table">';
      for (const key in p) {
          if (p.hasOwnProperty(key) && p[key] && key !== 'pincode' && key !== 'zip' && key !== 'postal_code') {
              const label = key.replace(/_/g, ' ').replace(/\\b\\w/g, l => l.toUpperCase());
              html += `<tr><td>${label}</td><td>${p[key]}</td></tr>`;
          }
      }
      html += '</table>';
      document.getElementById('modalBody').innerHTML = html;
      document.getElementById('detailModal').style.display = 'flex';
    }"""
    content = show_detail_pattern.sub(lambda m: dynamic_show_detail, content)

    meta_pattern = re.compile(r'const\s+meta\s*=\s*p\.districtname[^;]+;')
    new_meta = "const meta = (p.districtname || p.county || p.divisionname || '') + (p.statename || p.state || p.province ? ', ' + (p.statename || p.state || p.province) : '');"
    content = meta_pattern.sub(lambda m: new_meta, content)

    if orig != content:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        fixed_count += 1
print(f'Fixed UI across {fixed_count} HTML files!')
