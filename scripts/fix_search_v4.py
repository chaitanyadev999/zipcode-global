import os
import re

pages_dir = r"C:\Users\recla\zipcode-global\pages"

new_func = """// ── SEARCH ───────────────────────────────────────────────────
window.doSearch = async function(){
  const q=$('search').value.trim().toLowerCase(); if(!q)return;
  const origPh = $('search').placeholder;
  $('search').placeholder = "Searching...";
  
  if(!NAV.data.length && !globalIndex) {
      await loadGlobalIndex();
  }
  $('search').placeholder = origPh;
  
  const countrySlug = C.name.toLowerCase().replace(/ /g, '-').replace(/_/g, '-').replace(/&/g, 'and');
  
  let targetUrl = null;
  if (globalIndex) {
      if (globalIndex.pincodes && globalIndex.pincodes[q]) targetUrl = globalIndex.pincodes[q];
      else if (globalIndex.cities && globalIndex.cities[q]) targetUrl = globalIndex.cities[q];
  }
  
  if (targetUrl) {
      const parts = targetUrl.split('/');
      if (parts.length >= 3 && parts[1] === countrySlug) {
          const stateSlug = parts[2];
          if (!NAV.data.length || !NAV.stateFile || !NAV.stateFile.toLowerCase().startsWith(stateSlug)) {
              const stateObj = states.find(s => s.name.toLowerCase().startsWith(stateSlug));
              if(stateObj) {
                  const label = stateObj.name.replace('.json','').replace(/-/g,' ').replace(/\\b\\w/g,x=>x.toUpperCase());
                  await selectState(stateObj.name, label);
                  await new Promise(r => setTimeout(r, 100));
              }
          }
      }
  }

  if(NAV.data.length){
    let hits = NAV.data.filter(r => String(r.pincode || r.zip || r.postal_code || '').toLowerCase().trim() === q);
    
    if(!hits.length){
        hits = NAV.data.filter(r => String(r.officename || r.city || r.place_name || '').toLowerCase().trim() === q);
    }
    
    if(!hits.length){
        hits = NAV.data.filter(r=>Object.values(r).some(v=>String(v).toLowerCase().includes(q)));
    }
    
    if(hits.length){
      const isExact = hits.length === 1 && (
        String(hits[0].pincode || hits[0].zip || hits[0].postal_code || '').toLowerCase().trim() === q ||
        String(hits[0].officename || hits[0].city || hits[0].place_name || '').toLowerCase().trim() === q
      );
      
      if (isExact) {
          NAV.city = 'Search'; NAV.district = 'Results';
          showPinDetails(hits[0]); 
          toast('Found exact match!','ok');
          return;
      }
      
      NAV.city='Search'; NAV.district='Results';
      showPins(hits);
      updateMapMarkers(hits, 'Search: ' + q);
      toast('Found '+hits.length+' results','ok');
      return;
    }
  }
  
  toast('No results found for "'+q+'"', 'err');
}"""

updated = 0
for file in os.listdir(pages_dir):
    if not file.endswith('.html'): continue
    if file in ('country-template.html', 'about.html', 'contact.html', 'privacy.html', 'terms.html', 'disclaimer.html'): continue
    
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We use a broad regex that matches from // ── SEARCH ── up to the end of the function
    pattern = re.compile(r"// ── SEARCH ─+[\s\S]*?toast\('No results found for \"'\+q\+'\"','err'\);\s*\}")
    match = pattern.search(html)
    if match:
        html = html.replace(match.group(0), new_func)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        updated += 1
    else:
        # Check if it was already updated or has slightly different quotes
        pattern2 = re.compile(r"// ── SEARCH ─+[\s\S]*?toast\('No results found for \"'\+q\+'\"', 'err'\);\s*\}")
        match2 = pattern2.search(html)
        if match2:
            html = html.replace(match2.group(0), new_func)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            updated += 1

print(f"Updated {updated} HTML files with new search logic.")
