import os
import re

html = open(r'C:\Users\recla\zipcode-global\pages\india\andhra-pradesh.html', encoding='utf-8').read()
matches = re.findall(r'href=[\'"]https://chaitanyadev999\.github\.io/pincode-dataindia/([^"\'\n]+)[\'"]', html)
print("HREF MATCHES:")
for m in set(matches):
    print(m)

matches_src = re.findall(r'src=[\'"]https://chaitanyadev999\.github\.io/pincode-dataindia/([^"\'\n]+)[\'"]', html)
print("\nSRC MATCHES:")
for m in set(matches_src):
    print(m)
