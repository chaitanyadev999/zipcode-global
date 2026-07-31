import re

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"  const find = \(\.\.\.pats\) => k\.find\(x => pats\.some\(p => p\.test\(x\.toLowerCase\(\)\)\)\) \|\| '';"

new_find = """  const find = (...pats) => {
    for(const p of pats){
      const match = k.find(x => p.test(x.toLowerCase()));
      if(match) return match;
    }
    return '';
  };"""

content, count = re.subn(pattern, new_find, content)

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Replaced {count} instances.")
