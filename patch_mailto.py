import os

template_file = r'C:\Users\recla\zipcode-global\pages\country-template.html'

with open(template_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the mailto link in the result card
old_link = """<a class="action-btn" href="mailto:reclaimedmindwithrelaxmusic@gmail.com?subject=Mistake: ' + office + '">⚠️ Report</a>"""
new_link = """<a class="action-btn" href="/pages/report.html?code=' + COUNTRY.code + '&office=' + encodeURIComponent(office) + '&pin=' + encodeURIComponent(pin) + '">⚠️ Report</a>"""

if old_link in content:
    content = content.replace(old_link, new_link)
    with open(template_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced mailto link in country-template.html")
else:
    print("Could not find the mailto link in country-template.html")
