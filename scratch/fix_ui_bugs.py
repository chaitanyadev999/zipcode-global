import re
import os

base = r"C:\Users\recla\zipcode-global\pages"

def fix_html(file):
    path = os.path.join(base, file)
    if not os.path.exists(path): return
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Fix regex priority: put ^city$ before divisionname
    content = content.replace(
        r'city:  find(/division.?name/,/region.?name/,/^city$/,/^village$/,/^town$/,/place.?name/,/office.?name/,/^locality$/),',
        r'city:  find(/^city$/,/^village$/,/^town$/,/place.?name/,/office.?name/,/^locality$/,/division.?name/,/region.?name/),'
    )
    
    # Change "Divisions" to "Cities" for IN
    content = content.replace(
        r"C.code==='IN' ? ' — Divisions' : ' — Cities'",
        r"' — Cities'"
    )
    content = content.replace(
        r"C.code==='IN'?'Division':'City'",
        r"'City'"
    )
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        
fix_html('india.html')
fix_html('usa.html')
print("Fixed india.html and usa.html")

path_js = os.path.join(base, 'shared_pseo.js')
with open(path_js, 'r', encoding='utf-8') as f:
    js = f.read()

# Fix district fallback to include Districtname and Taluk
js = js.replace(
    r"const district = item.district || item.County || item.City || '';",
    r"const district = item.district || item.Districtname || item.County || item.City || item.Taluk || item.divisionname || '';"
)
js = js.replace(
    r"const district = (item.district || item.County || '').toLowerCase();",
    r"const district = (item.district || item.Districtname || item.County || '').toLowerCase();"
)
js = js.replace(
    r"'City', 'district', 'County', 'statename', 'State'",
    r"'City', 'district', 'Districtname', 'County', 'statename', 'State'"
)

with open(path_js, 'w', encoding='utf-8') as f:
    f.write(js)
    
print("Fixed shared_pseo.js")
