import re

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_find = "    const find = (...pats) => k.find(x => pats.some(p => p.test(x.toLowerCase()))) || '';"
new_find = """    const find = (...pats) => {
      for(const p of pats){
        const match = k.find(x => p.test(x.toLowerCase()));
        if(match) return match;
      }
      return '';
    };"""

content = content.replace(old_find, new_find)

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_pages.py find function updated successfully!")
