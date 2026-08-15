import os
import re

txt = open(r'C:\Users\recla\zipcode-global\pages\india.html', encoding='utf-8').read()
idx = txt.find('fetch(')
if idx != -1:
    print(txt[max(0, idx-100):idx+500])
else:
    print("Not found")
