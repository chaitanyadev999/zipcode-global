import os
import re

filepath = r"C:\Users\recla\zipcode-global\pages\country-template.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add sanitizeData function and update loadStates, selectState, doSearch
sanitize_js = """
// ── SANITIZE DATA ───────────────────────────────────────────────
function sanitizeData(data) {
  const seen = new Set();
  const cleaned = [];
  for (const r of data) {
    if (r.district && (r.district === 'Na' || r.district === 'NA')) continue;
    if (r.City && (r.City === 'Na' || r.City === 'NA')) continue;
    
    if (r.district) r.district = r.district.trim().replace(/\\w\\S*/g, w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase());
    if (r.City) r.City = r.City.trim().replace(/\\w\\S*/g, w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase());
    
    const sig = (r.pincode||r.ZipCode||'') + '|' + (r.district||'') + '|' + (r.City||'');
    if (!seen.has(sig)) {
      seen.add(sig);
      cleaned.push(r);
    }
  }
  return cleaned;
}
"""

html = html.replace("// ── FIELD DETECTOR ──────────────────────────────────────────────", sanitize_js + "\n// ── FIELD DETECTOR ──────────────────────────────────────────────")

# Update loadStates
loadStatesOld = "const states = files.filter(f=>f.name.endsWith('.json'));"
loadStatesNew = "const states = files.filter(f=>f.name.endsWith('.json'));\n    window.ALL_STATE_FILES = states;"
html = html.replace(loadStatesOld, loadStatesNew)

# Update selectState
selectStateOld = "NAV.data = await r.json();"
selectStateNew = "let rawData = await r.json();\n    NAV.data = sanitizeData(rawData);"
html = html.replace(selectStateOld, selectStateNew)

# Update doSearch
doSearchOld = """function doSearch(){
  const q=$('search').value.trim().toLowerCase(); if(!q)return;
  if(!NAV.data.length){toast('Select a region first','info');return;}
  const hits = NAV.data.filter(r=>Object.values(r).some(v=>String(v).toLowerCase().includes(q)));
  if(!hits.length){toast('No results found','err');return;}
  NAV.city='Search'; NAV.district='Results';
  showPins(hits);
  updateMapMarkers(hits, 'Search: ' + q);
  toast('Found '+hits.length+' results','ok');
}"""

doSearchNew = """async function doSearch(){
  const q=$('search').value.trim().toLowerCase(); if(!q)return;
  
  if(!NAV.data.length){
    if (!window.ALL_STATE_FILES || !window.ALL_STATE_FILES.length) {
      toast('Region data loading, please wait...','info');
      return;
    }
    toast('Searching entire country, this may take a moment...', 'info');
    $('search').disabled = true;
    try {
      const promises = window.ALL_STATE_FILES.map(f => fetch(C.dataBase + f.name).then(r => r.json()));
      const resultsArray = await Promise.all(promises);
      let allData = [];
      for (const data of resultsArray) {
        allData = allData.concat(data);
      }
      NAV.data = sanitizeData(allData);
      NAV.fields = detectFields(NAV.data);
    } catch(e) {
      toast('Failed to load country data for search', 'err');
      $('search').disabled = false;
      return;
    }
    $('search').disabled = false;
  }
  
  const hits = NAV.data.filter(r=>Object.values(r).some(v=>String(v).toLowerCase().includes(q)));
  if(!hits.length){toast('No results found','err');return;}
  NAV.city='Search'; NAV.district='Results';
  showPins(hits);
  updateMapMarkers(hits, 'Search: ' + q);
  toast('Found '+hits.length+' results','ok');
}"""
html = html.replace(doSearchOld, doSearchNew)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated country-template.html with search & sanitize fixes.")
