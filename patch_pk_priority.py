import re
import os

# 1. Update generate_pages.py
gen_file = r'C:\Users\recla\zipcode-global\generate_pages.py'
with open(gen_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove extractFlagTheme from the JS template inside generate_pages.py
extract_pattern = r"\s*// ── EXTRACT DYNAMIC THEME COLOR ──[\s\S]*?if\(fImg\) \{ fImg\.addEventListener\('load', function\(\) \{ extractFlagTheme\(this\); \}\); \}"
content = re.sub(extract_pattern, "", content)

with open(gen_file, 'w', encoding='utf-8') as f:
    f.write(content)


# 2. Update main.html
main_file = r'C:\Users\recla\zipcode-global\home\main.html'
with open(main_file, 'r', encoding='utf-8') as f:
    main_content = f.read()

# Remove 'PK' from PRIORITY (which is what the user probably means by footer prominence)
main_content = main_content.replace("'PK',", "")

# Slow down animation speeds
main_content = main_content.replace("animation: scrollX 350s", "animation: scrollX 1500s")
main_content = main_content.replace("const duration = 400 +", "const duration = 1200 +")

with open(main_file, 'w', encoding='utf-8') as f:
    f.write(main_content)


# 3. Update country-template.html
template_file = r'C:\Users\recla\zipcode-global\pages\country-template.html'
with open(template_file, 'r', encoding='utf-8') as f:
    tpl_content = f.read()

# Remove extractFlagTheme if present
tpl_content = re.sub(extract_pattern, "", tpl_content)

with open(template_file, 'w', encoding='utf-8') as f:
    f.write(tpl_content)

print("Restored 121 countries, removed PK from Priority list, removed canvas extraction, and slowed down animations.")
