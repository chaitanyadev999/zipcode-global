import os, glob, json, re

print('1. Checking newly created files:')
files_to_check = ['home/main.html', 'pages/world.html', 'postal-code-of-my-location.html', 'pages/postal-code-of-my-location.html']
for f in files_to_check:
    exists = os.path.exists(f)
    size = os.path.getsize(f) if exists else 0
    print(f'   {f}: exists={exists}, size={size} bytes')

print('\n2. Validating JSON-LD across all HTML files:')
bad = 0
all_html = glob.glob('*.html') + glob.glob('pages/*.html')
for f in all_html:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    matches = re.findall(r'<script\s+type=[\"\']application/ld\+json[\"\']>(.*?)</script>', c, re.DOTALL)
    for i, s in enumerate(matches):
        try:
            json.loads(s.strip())
        except Exception as e:
            print(f'   FAIL in {f} block {i}: {e}')
            bad += 1
print(f'   Total HTML files checked: {len(all_html)}')
print(f'   Total JSON-LD errors: {bad}')

print('\n3. Checking for lingering ${m.path} or /home/main.html:')
found_m = 0
found_main = 0
for f in all_html:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    if '${m.path}' in c:
        print(f'   ${{m.path}} in {f}')
        found_m += 1
    if '/home/main.html' in c:
        print(f'   /home/main.html in {f}')
        found_main += 1
print(f'   Lingering ${{m.path}}: {found_m}')
print(f'   Lingering /home/main.html links: {found_main}')
