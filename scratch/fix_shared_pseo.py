import re
file_path = r'C:\Users\recla\zipcode-global\pages\shared_pseo.js'
with open(file_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Add getBasePath() function if not exists
if 'function getBasePath()' not in js:
    js = 'function getBasePath() {\n    const path = window.location.pathname;\n    const idx = path.indexOf("/pages/");\n    return idx !== -1 ? path.substring(0, idx + 1) : "/";\n}\n' + js

js = js.replace("'https://chaitanyadev999.github.io/pincode-dataindia/pages/shared_pseo.js'", "getBasePath() + 'pages/shared_pseo.js'")
js = js.replace("'https://chaitanyadev999.github.io/pincode-dataindia/pages/report.html?country='", "getBasePath() + 'pages/report.html?country='")
js = js.replace('"https://chaitanyadev999.github.io/pincode-dataindia/pages/${COUNTRY.flagCode}.html"', '`${getBasePath()}pages/${COUNTRY.flagCode}.html`')
js = js.replace("'https://chaitanyadev999.github.io/pincode-dataindia/pages/country-template.html'", "getBasePath() + 'pages/country-template.html'")
js = js.replace("'https://chaitanyadev999.github.io/pincode-dataindia/home/assets/logo.png'", "getBasePath() + 'home/assets/logo.png'")
js = js.replace("'href=\"https://chaitanyadev999.github.io/pincode-dataindia/home/main.html\"'", "'href=\"' + getBasePath() + 'home/main.html\"'")
js = js.replace("'href=\"https://chaitanyadev999.github.io/pincode-dataindia/pages/'", "'href=\"' + getBasePath() + 'pages/'")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed shared_pseo.js!")
