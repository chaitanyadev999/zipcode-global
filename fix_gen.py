with open("C:/Users/recla/zipcode-global/generate_pages.py", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("langs = COUNTRY_LANGS.get(c.code, \"en,es,fr,de,zh-CN,ar,hi,pt,ru,ja\")", "langs = COUNTRY_LANGS.get(c.code.lower(), \"en,es,fr,de,zh-CN,ar,hi,pt,ru,ja\")")

with open("C:/Users/recla/zipcode-global/generate_pages.py", "w", encoding="utf-8") as f:
    f.write(content)
