import os

# Fix main.html
path = r'C:\Users\recla\zipcode-global\home\main.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix SPECIAL dict
html = html.replace(
    "'IN':'/pages/india.html','US':'/pages/usa.html','GB':'/pages/uk.html','CA':'/pages/canada.html'", 
    "'IN':'../pages/india.html','US':'../pages/usa.html','GB':'../pages/uk.html','CA':'../pages/canada.html'"
)
# Fix pageUrl
html = html.replace("||('/pages/'+code.toLowerCase()+'.html')", "||('../pages/'+code.toLowerCase()+'.html')")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

# Fix shared_pseo.js
path_js = r'C:\Users\recla\zipcode-global\pages\shared_pseo.js'
with open(path_js, 'r', encoding='utf-8') as f:
    js = f.read()

# Instead of absolute paths, use URL that is computed from SCRIPT_URL
# Or just replace "/pages/" with "https://zipcodeglobal.github.io/pages/" for absolute safety on local
js = js.replace('"/pages/', '"https://zipcodeglobal.github.io/pages/')
js = js.replace("'/pages/", "'https://zipcodeglobal.github.io/pages/")
# Also the currentScript default
js = js.replace("'/pages/shared_pseo.js'", "'https://zipcodeglobal.github.io/pages/shared_pseo.js'")

with open(path_js, 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed links!")
