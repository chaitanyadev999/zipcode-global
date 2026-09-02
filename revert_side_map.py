import os
import re

pages_dir = r"C:\Users\recla\zipcode-global\pages"

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content

    # Find and remove the injected media query block
    pattern = r"\s*@media\(min-width:1150px\)\{.*?\}\s*</style>"
    content = re.sub(pattern, "\n</style>", content, flags=re.DOTALL)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for file in os.listdir(pages_dir):
    if file.endswith('.html'):
        filepath = os.path.join(pages_dir, file)
        if os.path.isfile(filepath):
            if patch_file(filepath):
                count += 1

print(f"Reverted side map CSS in {count} country files successfully.")
