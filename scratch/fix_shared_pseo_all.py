import re
file_path = r'C:\Users\recla\zipcode-global\pages\shared_pseo.js'
with open(file_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace any occurrence of the domain with getBasePath()
js = re.sub(r'[\'"]https://chaitanyadev999\.github\.io/pincode-dataindia/(.*?)[\'"]', r'getBasePath() + "\1"', js)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed shared_pseo.js completely!")
