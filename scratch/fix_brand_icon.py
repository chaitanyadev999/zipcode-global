import glob

for fpath in glob.glob(r'C:\Users\recla\zipcode-global\pages\*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<div class="brand-icon">' in content and '.bmark' in content:
        new_content = content.replace('.bmark', '.brand-icon')
        with open(fpath, 'w', encoding='utf-8') as out_f:
            out_f.write(new_content)
        print(f'Fixed {fpath}')
