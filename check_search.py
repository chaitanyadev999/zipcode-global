import os

txt = open(r'C:\Users\recla\zipcode-global\pages\india.html', encoding='utf-8').read()
idx = txt.rfind('function doSearch')
if idx != -1:
    print(txt[max(0, idx-100):idx+500])
else:
    idx2 = txt.rfind('window.doSearch')
    if idx2 != -1:
        print(txt[max(0, idx2-100):idx2+500])
    else:
        print("doSearch not found")
