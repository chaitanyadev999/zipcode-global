import re
import os

files = [
    r'C:\Users\recla\zipcode-global\generate_pages.py',
    r'C:\Users\recla\zipcode-global\pages\india.html',
    r'C:\Users\recla\zipcode-global\pages\usa.html',
    r'C:\Users\recla\zipcode-global\pages\country-template.html'
]

new_code = """  // ── EXTRACT DYNAMIC THEME COLOR ──
  function extractFlagTheme(img) {
    try {
      if(!img.naturalWidth) return;
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
      canvas.width = img.naturalWidth; canvas.height = img.naturalHeight;
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      const data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
      let r=0, g=0, b=0, count=0;
      for(let i=0; i<data.length; i+=4) {
        if(data[i+3] > 128) { r += data[i]; g += data[i+1]; b += data[i+2]; count++; }
      }
      if(count > 0) {
        r = Math.floor(r/count); g = Math.floor(g/count); b = Math.floor(b/count);
        const max = Math.max(r,g,b);
        if (max < 150 && max > 0) { const mult = 180/max; r*=mult; g*=mult; b*=mult; }
        if (max === 0) { r=100; g=100; b=100; }
        const hex = '#' + [r,g,b].map(x => Math.floor(x).toString(16).padStart(2,'0')).join('');
        
        // Calculate a complementary/analogous accent color for --a
        // Simple hue rotation or just a brighter version
        let rA = Math.min(255, r + 40), gA = Math.max(0, g - 20), bA = Math.min(255, b + 60);
        const hexA = '#' + [rA,gA,bA].map(x => Math.floor(x).toString(16).padStart(2,'0')).join('');
        
        document.documentElement.style.setProperty('--p', hex);
        document.documentElement.style.setProperty('--a', hexA);
        document.documentElement.style.setProperty('--p2', `${Math.floor(r)},${Math.floor(g)},${Math.floor(b)}`);
      }
    } catch(e) { console.warn('CORS or Canvas error', e); }
  }
  const fImg = $('hFlag');
  if(fImg && fImg.complete) { extractFlagTheme(fImg); }
  if(fImg) { fImg.addEventListener('load', function() { extractFlagTheme(this); }); }"""

for file_path in files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(
        r"  // ── EXTRACT DYNAMIC THEME COLOR ──\s*function extractFlagTheme\(img\) \{[\s\S]*?\}\s*\}\s*const fImg = \$\('hFlag'\);\s*if\(fImg && fImg\.complete\) \{ extractFlagTheme\(fImg\); \}\s*if\(fImg\) \{ fImg\.addEventListener\('load', function\(\) \{ extractFlagTheme\(this\); \}\); \}",
        new_code,
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {file_path}")

