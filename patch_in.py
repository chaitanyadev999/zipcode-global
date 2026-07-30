import re

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace dataBase logic
old_db = "  dataBase:'https://cdn.jsdelivr.net/gh/chaitanyadev999/pincode-dataindia@main/world/{{CODE}}/'"
new_db = "  dataBase: '{{CODE}}' === 'IN' ? 'https://cdn.jsdelivr.net/gh/chaitanyadev999/pincode-dataindia@main/' : 'https://cdn.jsdelivr.net/gh/chaitanyadev999/pincode-dataindia@main/world/{{CODE}}/'"
content = content.replace(old_db, new_db)

# Replace fetch github API logic
old_api = "const r = await fetch('https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/'+C.code);"
new_api = """const apiUrl = C.code === 'IN' ? 'https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents' : 'https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/'+C.code;
      const r = await fetch(apiUrl);"""
content = content.replace(old_api, new_api)

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_pages.py updated successfully!")
