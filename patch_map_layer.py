import os

pages_dir = r"C:\Users\recla\zipcode-global\pages"

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content

    # Remove noWrap:true
    content = content.replace(', noWrap:true', '')
    
    # Change layer control position
    content = content.replace(
        'L.control.layers({"Map": osm, "Satellite": sat}).addTo(mainMap);',
        'L.control.layers({"Map": osm, "Satellite": sat}, null, {position: "bottomright"}).addTo(mainMap);'
    )
        
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

print(f"Fixed map wrapping and layer control position in {count} files successfully.")
