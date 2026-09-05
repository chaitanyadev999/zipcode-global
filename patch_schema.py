import re
import glob

count = 0
for f in glob.glob("pages/*.html"):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    if '"@type": "Dataset"' in content and '"creator"' not in content:
        new_content = re.sub(
            r'("keywords":\s*\[.*?\])',
            r'\1,\n        "creator": {\n          "@type": "Organization",\n          "name": "PO ZipCode Global",\n          "url": "https://pozip.me/"\n        },\n        "license": "https://creativecommons.org/licenses/by/4.0/"',
            content
        )
        if new_content != content:
            with open(f, "w", encoding="utf-8") as file:
                file.write(new_content)
            count += 1

print(f"Patched {count} files")
