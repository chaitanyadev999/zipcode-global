import re
with open(r'C:\Users\recla\zipcode-global\pages\jp.html', 'r', encoding='utf-8') as f:
    txt = f.read()

# Find the main IIFE block
start = txt.find("(function(){")
end = txt.rfind("})();") + 5
if start != -1 and end != -1:
    with open('test_script.js', 'w', encoding='utf-8') as f:
        f.write(txt[start:end])
