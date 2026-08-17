import glob
import os

files_to_check = ['index.html'] + glob.glob('pages/*.html')

for filepath in files_to_check:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Canonical URL
    content = content.replace('https://chaitanyadev999.github.io/pincode-dataindia/', 'https://pozip.me/')
    
    # 2. Update visible text for data credit
    content = content.replace('>chaitanyadev999/pincode-dataindia</a>', '>chaitanyadev999/zipcode-global</a>')
    
    # 3. Update href for the credit
    content = content.replace('href="https://github.com/chaitanyadev999/pincode-dataindia"', 'href="https://github.com/chaitanyadev999/zipcode-global"')
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated footers and canonical URLs.')
