import os

txt = open(r'C:\Users\recla\zipcode-global\pages\country-template.html', encoding='utf-8').read()
idx = txt.find('id="statRegions"')
print(txt[max(0, idx-100):idx+100])
