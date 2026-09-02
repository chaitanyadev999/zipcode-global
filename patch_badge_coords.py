import os
import re

pages_dir = r"C:\Users\recla\zipcode-global\pages"

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content

    # Move map-badge to bottom left
    content = content.replace('top:1rem;right:1rem;z-index:400;', 'bottom:1rem;left:1rem;z-index:400;top:auto;right:auto;')
    
    # Add coordinate swap logic in updateMapMarkers
    # We look for:
    # const lat = parseFloat(val(r,f.lat));
    # const lon = parseFloat(val(r,f.lon));
    # and replace with:
    # let lat = parseFloat(val(r,f.lat));
    # let lon = parseFloat(val(r,f.lon));
    # if (C.code === 'IN' && lat > 60 && lon < 45) { let temp = lat; lat = lon; lon = temp; }
    
    swap_code = """      let lat = parseFloat(val(r,f.lat));
      let lon = parseFloat(val(r,f.lon));
      if (C.code === 'IN' && lat > 60 && lon < 45) { let temp = lat; lat = lon; lon = temp; }"""
      
    # Regex to find the exact variable declarations
    pattern = r"const lat = parseFloat\(val\(r,f\.lat\)\);\s*const lon = parseFloat\(val\(r,f\.lon\)\);"
    content = re.sub(pattern, swap_code, content)
        
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

print(f"Patched badge and coords in {count} files successfully.")
