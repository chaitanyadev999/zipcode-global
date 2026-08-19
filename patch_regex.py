import os
import glob

old_regex = "city:  find(/division.?name/,/region.?name/,/^city$/,/^village$/,/^town$/,/place.?name/,/office.?name/,/^locality$/)"
new_regex = "city:  find(/^city$/,/office.?name/,/^village$/,/^town$/,/place.?name/,/^locality$/,/division.?name/,/region.?name/)"

def patch_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_regex in content:
            content = content.replace(old_regex, new_regex)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"Error on {filepath}: {e}")
    return False

# Patch generate_pages.py
if patch_file('generate_pages.py'):
    print("Patched generate_pages.py")

# Patch pages/*.html
patched_count = 0
for file in glob.glob('pages/*.html'):
    if patch_file(file):
        patched_count += 1

print(f"Patched {patched_count} HTML files in pages/ directory.")
