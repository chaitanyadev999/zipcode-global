import re
import os

files = [
    r'C:\Users\recla\zipcode-global\generate_pages.py',
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html'
]

for file_path in files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the extra closing brace
    bad_code = """    }
    }
    
    $('diGrid').innerHTML = realCityHtml + itemsHtml"""
    
    good_code = """    }
    
    $('diGrid').innerHTML = realCityHtml + itemsHtml"""

    content = content.replace(bad_code, good_code)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {file_path}")

