import os

base_dir = r'C:\Users\recla\zipcode-global\pages'
search_str = 'mailto:reclaimedmindwithrelaxmusic@gmail.com?subject=PO ZipCode Global'
replace_str = '/pages/report.html'
search_text = '>Email Us</a>'
replace_text = '>Contact / Report</a>'

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if search_str in content:
                    content = content.replace(search_str, replace_str)
                    content = content.replace(search_text, replace_text)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
            except Exception as e:
                pass

print(f"Updated {count} files.")
