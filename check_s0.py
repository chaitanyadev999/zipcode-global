import os

txt = open(r'C:\Users\recla\zipcode-global\pages\india.html', encoding='utf-8').read()
idx = txt.find('id="s0"')
print(txt[idx:idx+800])
