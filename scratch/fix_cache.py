import os

base_dir = r'C:\Users\recla\zipcode-global\pages'
count = 0

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace any version of shared_pseo.js or shared_pseo.css with a new version
                new_content = content.replace('shared_pseo.js?v=1.2', 'shared_pseo.js?v=1.3')
                new_content = new_content.replace('shared_pseo.js"', 'shared_pseo.js?v=1.3"')
                new_content = new_content.replace('shared_pseo.js\'', 'shared_pseo.js?v=1.3\'')
                
                # Also for CSS just in case
                new_content = new_content.replace('shared_pseo.css?v=1.2', 'shared_pseo.css?v=1.3')
                new_content = new_content.replace('shared_pseo.css"', 'shared_pseo.css?v=1.3"')
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
            except:
                pass

print(f"Updated cache buster in {count} HTML files.")
