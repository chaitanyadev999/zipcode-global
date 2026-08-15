import re

path = r'C:\Users\recla\zipcode-global\home\main.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure we add a div for the results if it doesn't exist
if 'id="finderResult"' not in html:
    # insert before the closing div of finder-wrapper
    html = html.replace('</button>\n    </div>\n  </div>\n</div>', 
                        '</button>\n    </div>\n    <div id="finderResult" style="display:none; margin-top:2rem; padding-top:1.5rem; border-top:1px solid rgba(0,212,255,0.2);"></div>\n  </div>\n</div>')

new_function = """window.gotoFinderCity = function() {
  const c = document.getElementById('fCountry').value;
  const st = document.getElementById('fState').value;
  const cy = document.getElementById('fCity').value;
  const resDiv = document.getElementById('finderResult');
  
  if(!c) {
    showToast('Please select a location first', 'error');
    return;
  }
  
  let cName = document.getElementById('fCountry').options[document.getElementById('fCountry').selectedIndex].text;
  let stName = document.getElementById('fState').selectedIndex > 0 ? document.getElementById('fState').options[document.getElementById('fState').selectedIndex].text : '';
  let cyName = document.getElementById('fCity').selectedIndex > 0 ? document.getElementById('fCity').options[document.getElementById('fCity').selectedIndex].text : '';
  
  let cSlug = cName.toLowerCase().replace(/ /g, '-').replace(/'/g, '');
  if (c === 'india') cSlug = 'india';
  if (c === 'usa') cSlug = 'usa';
  
  let targetUrl = '';
  if(cy) {
    targetUrl = cy;
  } else if(st) {
    targetUrl = 'pages/' + cSlug + '/' + st + '.html';
  } else if(c) {
    targetUrl = 'pages/' + (c === 'india' ? 'in' : (c === 'usa' ? 'us' : c)) + '.html';
  }
  
  let searchPlace = cyName || stName || cName;
  
  if (globalIndex && globalIndex.pincodes) {
     let matchedPins = [];
     for(let pin in globalIndex.pincodes) {
        let pUrl = globalIndex.pincodes[pin];
        if (pUrl === targetUrl || (targetUrl.endsWith('/') ? pUrl.startsWith(targetUrl) : pUrl.startsWith(targetUrl.replace('.html','/')))) {
           matchedPins.push(pin);
           if(matchedPins.length >= 8) break;
        }
     }
     
     // Fallback if no exact match (like selecting just a country)
     if (matchedPins.length === 0 && !cy && !st) {
       for(let pin in globalIndex.pincodes) {
          if (globalIndex.pincodes[pin].includes('pages/' + cSlug + '/')) {
             matchedPins.push(pin);
             if (matchedPins.length >= 8) break;
          }
       }
     }
     
     let pinsHtml = '';
     if (matchedPins.length > 0) {
       pinsHtml = '<div style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center; margin-bottom:1.5rem;">' + 
                  matchedPins.map(p => `<span style="background:rgba(0,212,255,0.15); color:var(--cyan); padding:8px 16px; border-radius:6px; font-weight:bold; font-size:1.2rem; border:1px solid rgba(0,212,255,0.3); box-shadow:0 0 10px rgba(0,212,255,0.1);">${p}</span>`).join('') +
                  '</div>';
     } else {
       pinsHtml = '<div style="text-align:center; color:#ccc; margin-bottom:1rem;">Select a more specific location to see exact Pincodes.</div>';
     }
     
     let gSearch = `https://www.google.com/search?q=${encodeURIComponent(searchPlace + ' postal code zip code')}`;
     let navUrl = targetUrl.startsWith('pages/') ? '../' + targetUrl : targetUrl;
     
     resDiv.style.display = 'block';
     resDiv.innerHTML = `
        <h4 style="text-align:center; color:#fff; margin-bottom:1rem;">Pincodes for ${searchPlace}:</h4>
        ${pinsHtml}
        <div style="display:flex; flex-wrap:wrap; gap:15px; justify-content:center;">
          <a href="${navUrl}" style="padding:10px 20px; background:var(--grad); color:#000; font-weight:bold; text-decoration:none; border-radius:8px; box-shadow:0 4px 15px rgba(0,212,255,0.2);">Find more pincodes here</a>
          <a href="${gSearch}" target="_blank" style="padding:10px 20px; background:rgba(255,255,255,0.1); color:#fff; font-weight:bold; text-decoration:none; border-radius:8px; border:1px solid rgba(255,255,255,0.3);">🌍 Google Search</a>
        </div>
     `;
  } else {
     showToast('Index not ready. Please wait...', 'warning');
  }
}
"""

html = re.sub(r'window\.gotoFinderCity\s*=\s*function\s*\(\)\s*\{.*?(?=\n// ── RENDER CARDS ──)', new_function + '\n\n', html, flags=re.DOTALL)
html = re.sub(r'function gotoFinderCity\s*\(\)\s*\{.*?(?=\n// ── RENDER CARDS ──)', new_function + '\n\n', html, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
