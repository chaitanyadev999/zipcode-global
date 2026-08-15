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
  
  const origPh = $('search').placeholder;
  $('search').placeholder = "Searching...";
  
  if(!NAV.data.length && !globalIndex) {
      await loadGlobalIndex();
  }
  $('search').placeholder = origPh;
  
  // 1. If global index has this exact pincode, load its state locally
  if (!NAV.data.length && globalIndex && globalIndex.pincodes && globalIndex.pincodes[q]) {
      const parts = globalIndex.pincodes[q].split('/'); // pages/in/andhra-pradesh/kakinada.html
      if (parts.length >= 3 && parts[1] === C.code.toLowerCase()) {
          const stateSlug = parts[2]; // andhra-pradesh
          // Try to find the exact JSON file in our states list
          const stateObj = states.find(s => s.name.toLowerCase().startsWith(stateSlug));
          if(stateObj) {
              const label = stateObj.name.replace('.json','').replace(/-/g,' ').replace(/\\b\\w/g,x=>x.toUpperCase());
              await window.selectState(stateObj.name, label);
              // Wait a tiny bit for render
              await new Promise(r => setTimeout(r, 100));
          }
      }
  }

  // 2. Search local data (which might have just been loaded above!)
  if(NAV.data.length){
    // Exact match for pincodes first
    let hits = NAV.data.filter(r => {
        const pin = String(r.pincode || r.zip || r.postal_code || '').toLowerCase().trim();
        return pin === q;
    });
    
    // If no exact pincode match, do partial match on all fields
    if(!hits.length){
        hits = NAV.data.filter(r=>Object.values(r).some(v=>String(v).toLowerCase().includes(q)));
    }
    
    if(hits.length){
      // If exact pincode match (1 hit) OR they searched a specific pincode
      if (hits.length === 1 && String(hits[0].pincode || hits[0].zip || hits[0].postal_code || '').toLowerCase().trim() === q) {
          // Auto-jump to Step 4!
          NAV.city = 'Search'; NAV.district = 'Results';
          showPinDetails(hits[0]); // Need to ensure this function exists or emulate it
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
  
  // 3. If not found locally, and we have global index, maybe redirect?
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
  toast('No results found for "'+q+'"','err');
}

// ── SHOW PIN DETAILS ────────────────────────────────────────────
window.showPinDetails = function(pinObj) {
  $('stGrid').style.display = 'none';
  $('cityGrid').style.display = 'none';
  $('distGrid').style.display = 'none';
  $('pinGrid').style.display = 'none';
  
  const d = $('pinDetails');
  d.style.display = 'block';
  $('s0').style.display = 'inline-block';
  $('s1').style.display = 'inline-block';
  $('s2').style.display = 'inline-block';
  $('s3').style.display = 'inline-block';
  
  let html = '<div class="pin-card highlight" style="max-width:600px;margin:0 auto;text-align:left;">';
  for(let k in pinObj){
      html += '<div style="margin-bottom:8px;"><strong>'+k.toUpperCase()+':</strong> '+pinObj[k]+'</div>';
  }
  const query = encodeURIComponent((pinObj.officename || pinObj.city || '') + ' ' + (pinObj.pincode || pinObj.zip || ''));
  html += '<div style="margin-top:15px;display:flex;gap:10px;">';
  html += '<a href="https://www.google.com/maps/search/?api=1&query='+query+'" target="_blank" class="btn">📍 Maps</a>';
  html += '<a href="https://www.google.com/search?q='+query+'" target="_blank" class="btn">🔍 Search</a>';
  html += '</div></div>';
  
  d.innerHTML = html;
  
  // Highlight visually
  setTimeout(() => {
      const card = d.querySelector('.pin-card');
      if(card) {
          card.style.boxShadow = '0 0 15px var(--accent)';
          card.style.transform = 'scale(1.02)';
          setTimeout(() => {
              card.style.transform = 'scale(1)';
          }, 300);
      }
  }, 50);
}
window.doSearch = doSearch; // legacy override
"""

for file in os.listdir(pages_dir):
    if not file.endswith('.html'): continue
    if file in ('country-template.html', 'about.html', 'contact.html', 'privacy.html', 'terms.html', 'disclaimer.html'): continue
    
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace from "// ── SEARCH " up to "window.doSearch = doSearch;"
    pattern = re.compile(r"// ── SEARCH ─+[\s\S]*?window\.doSearch = doSearch;")
    match = pattern.search(html)
    if match:
        old_text = match.group(0)
        new_html = html.replace(old_text, new_search)
        
        # We also need to add pinDetails div if it doesn't exist!
        if 'id="pinDetails"' not in new_html:
            new_html = new_html.replace('<div id="pinGrid" class="grid" style="display:none;"></div>', 
                                        '<div id="pinGrid" class="grid" style="display:none;"></div>\n      <div id="pinDetails" style="display:none;padding:20px;text-align:center;"></div>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        updated += 1

print(f"Updated {updated} files with advanced local search and auto-open details.")
