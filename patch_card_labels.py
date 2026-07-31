import re

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_labels = """      if(low === 'circlename') label = 'Circle Name';
      if(low === 'regionname') label = 'Region Name';
      if(low === 'divisionname') label = 'Division Name';
      if(low === 'officename') label = 'Office Name';"""

new_labels = """      if(low === 'circlename') label = 'Circle';
      if(low === 'regionname') label = 'Region';
      if(low === 'divisionname') label = 'City';
      if(low === 'officename') label = 'Post Office';"""

content = content.replace(old_labels, new_labels)

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_pages.py labels updated successfully!")
