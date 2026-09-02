import os
import re

pages_dir = r"C:\Users\recla\zipcode-global\pages"

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content

    # Add satellite layer to initMainMap
    if 'const sat =' not in content and 'function initMainMap()' in content:
        # We need to replace the internals of initMainMap()
        # Original:
        # function initMainMap(){
        #   if(mainMap) return;
        #   const mapEl = $('mainMap');
        #   if(!mapEl || typeof L === 'undefined') return;
        #   mainMap = L.map('mainMap', {zoomControl:true, attributionControl:false}).setView([C.lat, C.lon], 5);
        #   L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18, noWrap:true}).addTo(mainMap);
        #   mapMarkersGroup = L.layerGroup().addTo(mainMap);
        
        replacement = '''function initMainMap(){
  if(mainMap) return;
  const mapEl = $('mainMap');
  if(!mapEl || typeof L === 'undefined') return;
  const osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18, noWrap:true});
  const sat = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',{maxZoom:18, noWrap:true});
  mainMap = L.map('mainMap', {zoomControl:true, attributionControl:false, layers: [osm]}).setView([C.lat, C.lon], 5);
  L.control.layers({"Map": osm, "Satellite": sat}).addTo(mainMap);
  mapMarkersGroup = L.layerGroup().addTo(mainMap);'''

        # We will use regex to replace the function body up to mapMarkersGroup
        pattern = r"function initMainMap\(\)\{.*?mapMarkersGroup = L\.layerGroup\(\)\.addTo\(mainMap\);"
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
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

print(f"Patched map in {count} country files successfully.")
