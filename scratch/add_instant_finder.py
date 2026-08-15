import re

path = r'C:\Users\recla\zipcode-global\home\main.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

ui_block = """
<!-- INSTANT FINDER FORM -->
<div class="finder-wrapper" style="max-width:900px; margin:-30px auto 40px auto; position:relative; z-index:10; padding:0 15px;">
  <div style="background:rgba(10,14,39,0.95); backdrop-filter:blur(24px); border:1px solid rgba(0,212,255,0.3); border-radius:16px; padding:2rem; box-shadow:0 12px 50px rgba(0,0,0,0.6), 0 0 40px rgba(0,212,255,0.15);">
    <h3 style="color:var(--t); font-size:1.4rem; margin-bottom:0.5rem; text-align:center;">⚡ Instant Form Finder</h3>
    <p style="color:var(--t3); text-align:center; margin-bottom:1.5rem; font-size:0.95rem;">Select your location step-by-step to view all Postal & ZIP codes.</p>
    
    <div style="display:flex; flex-wrap:wrap; gap:1rem; align-items:flex-end; justify-content:center;">
      <div style="flex:1 1 200px;">
        <label style="color:var(--cyan); font-size:0.8rem; font-weight:bold; margin-bottom:0.4rem; display:block;">Country</label>
        <select id="fCountry" onchange="loadFinderStates()" style="width:100%; padding:0.8rem; background:rgba(0,0,0,0.5); border:1px solid rgba(0,212,255,0.3); color:#fff; border-radius:8px; outline:none; font-family:var(--fm); font-size:0.95rem;">
          <option value="">-- Select Country --</option>
        </select>
      </div>
      <div style="flex:1 1 200px;">
        <label style="color:var(--cyan); font-size:0.8rem; font-weight:bold; margin-bottom:0.4rem; display:block;">State / Province</label>
        <select id="fState" onchange="loadFinderCities()" disabled style="width:100%; padding:0.8rem; background:rgba(0,0,0,0.5); border:1px solid rgba(0,212,255,0.3); color:#fff; border-radius:8px; outline:none; font-family:var(--fm); font-size:0.95rem; opacity:0.5;">
          <option value="">-- Select State --</option>
        </select>
      </div>
      <div style="flex:1 1 200px;">
        <label style="color:var(--cyan); font-size:0.8rem; font-weight:bold; margin-bottom:0.4rem; display:block;">City / District</label>
        <select id="fCity" onchange="document.getElementById('finderBtn').style.transform='scale(1.05)'; setTimeout(()=>document.getElementById('finderBtn').style.transform='scale(1)',200);" disabled style="width:100%; padding:0.8rem; background:rgba(0,0,0,0.5); border:1px solid rgba(0,212,255,0.3); color:#fff; border-radius:8px; outline:none; font-family:var(--fm); font-size:0.95rem; opacity:0.5;">
          <option value="">-- Select City --</option>
        </select>
      </div>
      <button id="finderBtn" onclick="gotoFinderCity()" style="padding:0.8rem 1.5rem; border-radius:8px; background:var(--grad); border:none; color:#000; font-weight:bold; cursor:pointer; flex:0 1 auto; min-width:140px; transition:all 0.3s var(--ease); box-shadow:0 4px 15px rgba(0,212,255,0.2);">Get Pincodes 🚀</button>
    </div>
  </div>
</div>
"""

js_block = """
// ── INSTANT FINDER LOGIC ──
function initFinder() {
  const fC = document.getElementById('fCountry');
  if(!fC) return;
  fC.innerHTML = '<option value="">-- Select Country --</option>';
  let sorted = [...ALL].sort((a,b) => a.name.localeCompare(b.name));
  sorted.forEach(c => {
    let opt = document.createElement('option');
    let val = c.code.toLowerCase();
    if(val === 'in') val = 'india';
    if(val === 'us') val = 'usa';
    opt.value = val;
    opt.textContent = c.name;
    fC.appendChild(opt);
  });
}

function loadFinderStates() {
  const c = document.getElementById('fCountry').value;
  const s = document.getElementById('fState');
  const cy = document.getElementById('fCity');
  
  cy.innerHTML = '<option value="">-- Select City --</option>';
  cy.disabled = true;
  cy.style.opacity = '0.5';
  
  if(!c || !globalIndex || !globalIndex.states) {
    s.innerHTML = '<option value="">-- Select State --</option>';
    s.disabled = true;
    s.style.opacity = '0.5';
    return;
  }
  
  s.disabled = false;
  s.style.opacity = '1';
  s.innerHTML = '<option value="">-- Select State --</option>';
  
  const cPath = 'pages/' + c + '/';
  let statesFound = [];
  for(let key in globalIndex.states) {
    if(globalIndex.states[key].includes(cPath)) {
      statesFound.push({ name: key, path: globalIndex.states[key] });
    }
  }
  statesFound.sort((a,b) => a.name.localeCompare(b.name));
  
  statesFound.forEach(st => {
    let opt = document.createElement('option');
    // extract state slug from path
    let parts = st.path.split('/');
    opt.value = parts[2].replace('.html',''); 
    opt.textContent = st.name.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    s.appendChild(opt);
  });
}

function loadFinderCities() {
  const c = document.getElementById('fCountry').value;
  const st = document.getElementById('fState').value;
  const cy = document.getElementById('fCity');
  
  if(!c || !st || !globalIndex || !globalIndex.cities) {
    cy.innerHTML = '<option value="">-- Select City --</option>';
    cy.disabled = true;
    cy.style.opacity = '0.5';
    return;
  }
  
  cy.disabled = false;
  cy.style.opacity = '1';
  cy.innerHTML = '<option value="">-- Select City --</option>';
  
  const sPath = 'pages/' + c + '/' + st + '/';
  let citiesFound = [];
  for(let key in globalIndex.cities) {
    if(globalIndex.cities[key].includes(sPath)) {
      citiesFound.push({ name: key, path: globalIndex.cities[key] });
    }
  }
  citiesFound.sort((a,b) => a.name.localeCompare(b.name));
  
  citiesFound.forEach(city => {
    let opt = document.createElement('option');
    opt.value = city.path;
    opt.textContent = city.name.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    cy.appendChild(opt);
  });
}

function gotoFinderCity() {
  const c = document.getElementById('fCountry').value;
  const st = document.getElementById('fState').value;
  const cy = document.getElementById('fCity').value;
  
  if(cy) {
    window.location.href = '../' + cy;
  } else if(st) {
    window.location.href = '../pages/' + c + '/' + st + '.html';
  } else if(c) {
    window.location.href = '../pages/' + c + '.html';
  } else {
    showToast('Please select a location first', 'error');
  }
}
"""

if '<!-- INSTANT FINDER FORM -->' not in html:
    html = html.replace('</section>\n\n\n<!-- SCROLLING FLAGS', '</section>\n\n' + ui_block + '\n<!-- SCROLLING FLAGS')

if 'initFinder()' not in html:
    html = html.replace('// ── RENDER CARDS ──', js_block + '\n// ── RENDER CARDS ──')

# Ensure initFinder is called when globalIndex is loaded, OR immediately
# Since globalIndex is loaded async, we can call initFinder immediately (for countries)
# and when states/cities are needed, they use globalIndex
if 'initFinder();' not in html:
    html = html.replace('populateCountrySelect();', 'populateCountrySelect();\ninitFinder();')

# We must ensure globalIndex is loaded if they try to interact with the form.
# The user might select Country before globalIndex is loaded. Let's make sure loadFinderStates awaits globalIndex!
# Actually, loadFinderStates relies on globalIndex. It's better to preload it.
# We already have loadGlobalIndex(). We can call it inside initFinder().
fix_init = """
async function initFinder() {
  if(!globalIndex) { await loadGlobalIndex(); }
  const fC = document.getElementById('fCountry');
  if(!fC || fC.options.length > 1) return;
  fC.innerHTML = '<option value="">-- Select Country --</option>';
  let sorted = [...ALL].sort((a,b) => a.name.localeCompare(b.name));
  sorted.forEach(c => {
    let opt = document.createElement('option');
    let val = c.code.toLowerCase();
    if(val === 'in') val = 'india';
    if(val === 'us') val = 'usa';
    opt.value = val;
    opt.textContent = c.name;
    fC.appendChild(opt);
  });
}
"""
html = html.replace('function initFinder() {', 'async function initFinder() {')
if 'if(!globalIndex) { await loadGlobalIndex(); }' not in html:
    html = html.replace('const fC = document.getElementById(\'fCountry\');', 'if(!globalIndex) { await loadGlobalIndex(); }\n  const fC = document.getElementById(\'fCountry\');')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
