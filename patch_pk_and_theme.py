import re
import os
import glob

# 1. Update generate_pages.py
gen_file = r'C:\Users\recla\zipcode-global\generate_pages.py'
with open(gen_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Pakistan from DB
content = re.sub(r"\n\s*'PK':\s*\{'name':'Pakistan'.*?\},", "", content)

# Remove Pakistan from COUNTRY_THEMES
content = re.sub(r"\n\s*'PK':\s*\{'p':.*?\s*\},", "", content)

# Remove extractFlagTheme from the JS template inside generate_pages.py
extract_pattern = r"\s*// ── EXTRACT DYNAMIC THEME COLOR ──[\s\S]*?if\(fImg\) \{ fImg\.addEventListener\('load', function\(\) \{ extractFlagTheme\(this\); \}\); \}"
content = re.sub(extract_pattern, "", content)

with open(gen_file, 'w', encoding='utf-8') as f:
    f.write(content)


# 2. Update main.html
main_file = r'C:\Users\recla\zipcode-global\home\main.html'
with open(main_file, 'r', encoding='utf-8') as f:
    main_content = f.read()

# Remove PK from COUNTRIES
main_content = re.sub(r"\n\s*\{code:'PK',name:'Pakistan'.*?\},", "", main_content)

# Remove 'PK', from PRIORITY
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

# Remove PK from COUNTRY_DB
tpl_content = re.sub(r"\n\s*'PK':\s*\{name:'Pakistan'.*?\},", "", tpl_content)

with open(template_file, 'w', encoding='utf-8') as f:
    f.write(tpl_content)

print("Removed PK and extractFlagTheme, and slowed down animations.")
