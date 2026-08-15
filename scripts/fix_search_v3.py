import os
import json
import re
import sys

# 1. First, we need to extract the country map from generate_pages.py
sys.path.append(r"C:\Users\recla\zipcode-global")
try:
    import generate_pages
    COUNTRIES = generate_pages.COUNTRIES
except Exception as e:
    print(f"Error importing COUNTRIES: {e}")
    sys.exit(1)

def slugify(s):
    return str(s).lower().replace(' ', '-').replace('_', '-').replace('&', 'and')

# Create mapping of CC -> full slug
cc_to_slug = {}
for c in COUNTRIES:
    cc = c[0]
    name = c[1]
    cc_to_slug[cc] = slugify(name)

# 2. Re-generate search_index.json
data_repo = r"C:\Users\recla\zipcode-global\scratch\pincode-dataindia"
output_file = r"C:\Users\recla\zipcode-global\home\assets\search_index.json"

index = {
    "countries": {},
    "states": {},
    "cities": {},
    "pincodes": {}
}

# Add countries
for c in COUNTRIES:
    slug = slugify(c[1])
    index["countries"][c[1].lower()] = f"pages/{slug}.html"
# Hardcode common alternatives
index["countries"]["united states"] = "pages/united-states.html"
index["countries"]["usa"] = "pages/united-states.html"
index["countries"]["uk"] = "pages/united-kingdom.html"

def process_state_file(cc, state_file, filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except:
            return
            
    state_slug = slugify(state_file.replace('.json', ''))
    state_name = state_slug.replace('-', ' ')
    
    country_slug = cc_to_slug.get(cc, cc.lower())
    base_url = f"pages/{country_slug}/{state_slug}"
    
    index["states"][state_name] = f"{base_url}.html"
    
    for row in data:
        if not isinstance(row, dict): continue
        row_lower = {k.lower(): v for k, v in row.items()}
        pin = str(row_lower.get('pincode', row_lower.get('zip', row_lower.get('zipcode', row_lower.get('postal_code', row_lower.get('postcode', '')))))).strip()
        city = str(row_lower.get('officename', row_lower.get('city', row_lower.get('place_name', '')))).strip()
        
        if pin and pin not in index["pincodes"]:
            city_slug = slugify(city) if city else 'unknown-city'
            index["pincodes"][pin.lower()] = f"{base_url}/{city_slug}.html"
            
        if city:
            city_key = city.lower()
            if city_key not in index["cities"]:
                index["cities"][city_key] = f"{base_url}/{slugify(city)}.html"

print("Generating search index... (This may take a minute)")
# IN
in_files = [f for f in os.listdir(data_repo) if f.endswith('.json') and f not in ('pincode-map.json', 'package.json')]
for f in in_files:
    process_state_file('IN', f, os.path.join(data_repo, f))

# US
us_dir = os.path.join(data_repo, 'usa')
if os.path.exists(us_dir):
    for f in os.listdir(us_dir):
        if f.endswith('.json'): process_state_file('US', f, os.path.join(us_dir, f))

# World
world_dir = os.path.join(data_repo, 'world')
if os.path.exists(world_dir):
    for cc in os.listdir(world_dir):
        if cc in ('IN', 'US'): continue
        cc_dir = os.path.join(world_dir, cc)
        if os.path.isdir(cc_dir):
            for f in os.listdir(cc_dir):
                if f.endswith('.json'):
                    process_state_file(cc, f, os.path.join(cc_dir, f))

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(index, f)

print(f"Generated search index with {len(index['states'])} states, {len(index['cities'])} cities, and {len(index['pincodes'])} pincodes.")


# 3. Update the doSearch function in all HTML files
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
  
  toast('No results found for '+q, 'err');
}"""

updated = 0
for file in os.listdir(pages_dir):
    if not file.endswith('.html'): continue
    if file in ('country-template.html', 'about.html', 'contact.html', 'privacy.html', 'terms.html', 'disclaimer.html'): continue
    
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    pattern = re.compile(r"// ── SEARCH ─+[\s\S]*?toast\('No results found for '\+q, 'err'\);\s*\}")
    match = pattern.search(html)
    if match:
        html = html.replace(match.group(0), new_func)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        updated += 1

print(f"Updated {updated} HTML files with new search logic.")
