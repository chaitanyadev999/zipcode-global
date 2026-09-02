import os
import re

pages_dir = r"C:\Users\recla\zipcode-global\pages"

css_block = """  @media(min-width:1150px){
    body { padding-right: 420px; }
    .interactive-map-sec {
      position: fixed !important;
      right: 1.5rem;
      top: 90px;
      width: 380px;
      margin: 0 !important;
      padding: 0 !important;
      z-index: 500;
    }
    .map-card-shell { height: calc(100vh - 110px) !important; max-height: 800px; }
  }
</style>"""

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content

    if 'body { padding-right: 420px; }' not in content:
        content = content.replace('</style>', css_block)
        
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

print(f"Patched side map CSS in {count} country files successfully.")
