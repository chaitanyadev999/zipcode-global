import os
target = "Browse Countries by Region"
for r, d, f in os.walk(r'C:\Users\recla\zipcode-global'):
    for file in f:
        if file.endswith('.html') or file.endswith('.js'):
            try:
                if target in open(os.path.join(r, file), 'r', encoding='utf-8', errors='ignore').read():
                    print("FOUND IN:", os.path.join(r, file))
            except:
                pass
print("Done")
