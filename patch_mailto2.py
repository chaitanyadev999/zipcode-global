import os

template_file = r'C:\Users\recla\zipcode-global\pages\country-template.html'

with open(template_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the PREVIOUSLY patched link with the correct one that uses COUNTRY.name
old_link = """<a class="action-btn" href="/pages/report.html?code=' + COUNTRY.code + '&office=' + encodeURIComponent(office) + '&pin=' + encodeURIComponent(pin) + '">⚠️ Report</a>"""
new_link = """<a class="action-btn" href="/pages/report.html?country=' + encodeURIComponent(COUNTRY.name) + '&office=' + encodeURIComponent(office) + '&pin=' + encodeURIComponent(pin) + '">⚠️ Report</a>"""

if old_link in content:
    content = content.replace(old_link, new_link)
    with open(template_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced link to use COUNTRY.name in country-template.html")
else:
    print("Could not find the patched link in country-template.html")
