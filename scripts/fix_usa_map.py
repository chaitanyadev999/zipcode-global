import os

filepath = r"C:\Users\recla\zipcode-global\pages\usa.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("lat:37.0902, lon:-95.7129", "lat:39.8283, lon:-98.5795")
html = html.replace(".setView([C.lat, C.lon], 5)", ".setView([C.lat, C.lon], 4)")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated USA map center")
