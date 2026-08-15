import os
import re

pages_dir = r"C:\Users\recla\zipcode-global\pages"
updated = 0

new_func = """// ── SHOW PIN DETAILS ────────────────────────────────────────────
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
  const office = pinObj.officename || pinObj.City || pinObj.OfficeName || '';
  const state = pinObj.statename || pinObj.State || '';
  const pin = pinObj.pincode || pinObj.zip || pinObj.ZipCode || '';
  const query = encodeURIComponent(office + ' ' + pin);
  
  html += '<div style="margin-top:15px;display:flex;gap:10px;flex-wrap:wrap;">';
  html += '<a href="https://www.google.com/maps/search/?api=1&query='+query+'" target="_blank" class="btn">📍 Maps</a>';
  html += '<a href="https://www.google.com/search?q='+encodeURIComponent('About ' + office + ' ' + state)+'" target="_blank" class="btn" style="background:linear-gradient(135deg, #10a37f, #0d8a6a);">📖 About '+office+'</a>';
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
window.doSearch = doSearch;"""

for file in os.listdir(pages_dir):
    if not file.endswith('.html'): continue
    if file in ('country-template.html', 'about.html', 'contact.html', 'privacy.html', 'terms.html', 'disclaimer.html'): continue
    
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    pattern = re.compile(r"// ── SHOW PIN DETAILS ─+[\s\S]*?window\.doSearch = doSearch;")
    match = pattern.search(html)
    if match:
        old_text = match.group(0)
        new_html = html.replace(old_text, new_func)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        updated += 1

print(f"Updated {updated} files with About City button.")
