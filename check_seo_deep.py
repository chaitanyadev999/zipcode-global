import os

target = "ZIP Code vs PIN Code vs Postal Code"

for root, _, files in os.walk('pages'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    count = content.count(target)
                    if count > 0:
                        print(f'{filepath}: {count} times')
            except Exception as e:
                pass
