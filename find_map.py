import sys
with open('pages/country-template.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'id="map"' in line or 'mapSection' in line:
            print(f'Line {i+1}: {line.strip()}')
