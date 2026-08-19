import glob
import sys

target = "ZIP Code vs PIN Code"

for f in glob.glob('*.html') + glob.glob('pages/*.html') + glob.glob('pages/*.js') + glob.glob('*.js'):
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            count = content.count(target)
            if count > 0:
                print(f'{f}: {count} times')
    except Exception as e:
        pass
