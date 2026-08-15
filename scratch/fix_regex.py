path = r'C:\Users\recla\zipcode-global\home\main.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()
    
html = html.replace("city.name.replace(/-/g, ' ').replace(/ \\w/g, l => l.toUpperCase())", "city.name.replace(/-/g, ' ').replace(/\\b\\w/g, l => l.toUpperCase())")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
