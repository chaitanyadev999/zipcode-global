import os
import re

pages_dir = r"C:\Users\recla\zipcode-global\pages"
updated = 0

new_search = """// ── SEARCH ──────────────────────────────────────────────────────
let globalIndex = null;
async function loadGlobalIndex() {
  if (!globalIndex) {
     try {
       const res = await fetch('../home/assets/search_index.json');
       if (res.ok) globalIndex = await res.json();
     } catch (e) {}
  }
}
$('search').addEventListener('focus', loadGlobalIndex);

window.doSearch = async function(){
  const q=$('search').value.trim().toLowerCase(); if(!q)return;
  
  if(NAV.data.length){
    const hits = NAV.data.filter(r=>Object.values(r).some(v=>String(v).toLowerCase().includes(q)));
    if(hits.length){
      NAV.city='Search'; NAV.district='Results';
      showPins(hits);
      updateMapMarkers(hits, 'Search: ' + q);
      toast('Found '+hits.length+' results','ok');
      return;
    }
  }
  
  const origPh = $('search').placeholder;
  $('search').placeholder = "Searching global index...";
  if (!globalIndex) await loadGlobalIndex();
  $('search').placeholder = origPh;
  
  if (globalIndex) {
      if (globalIndex.pincodes && globalIndex.pincodes[q]) {
          window.location.href = '../' + globalIndex.pincodes[q];
          return;
      }
      const cKey = q.replace(/[^a-z0-9\\s-]/g, '').trim().replace(/\\s+/g, '-');
      if (globalIndex.cities && globalIndex.cities[cKey]) {
          window.location.href = '../' + globalIndex.cities[cKey];
          return;
      }
      const sKey = q.replace(/[^a-z0-9\\s-]/g, '').trim().replace(/\\s+/g, ' ');
      if (globalIndex.states && globalIndex.states[sKey]) {
          window.location.href = '../' + globalIndex.states[sKey];
          return;
      }
  }
  toast('No results found','err');
}
window.doSearch = doSearch; // legacy
"""

for file in os.listdir(pages_dir):
    if not file.endswith('.html'): continue
    if file == 'country-template.html': continue
    if file == 'about.html': continue
    if file == 'contact.html': continue
    if file == 'privacy.html': continue
    if file == 'terms.html': continue
    if file == 'disclaimer.html': continue
    
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We replace from "// ── SEARCH " up to "window.doSearch = doSearch;"
    pattern = re.compile(r"// ── SEARCH ─+[\s\S]*?window\.doSearch = doSearch;")
    match = pattern.search(html)
    if match:
        old_text = match.group(0)
        new_html = html.replace(old_text, new_search)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        updated += 1

print(f"Updated {updated} files with new search logic.")
