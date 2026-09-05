import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

btn_html = '''</button>
        <button id="locateBtn" onclick="findMyLocation()" style="padding:0.8rem 1.5rem; border-radius:8px; background:rgba(0,212,255,0.1); border:1px solid var(--p); color:var(--p); font-weight:bold; cursor:pointer; flex:0 1 auto; min-width:140px; transition:all 0.3s var(--ease);">📍 Find My Location</button>
      </div>
      <div id="finderResult"'''

html = html.replace('</button>\n      </div>\n      <div id="finderResult"', btn_html)

# Now we need to append the JS function at the end of the <script> block
js_function = '''
  async function findMyLocation() {
    const btn = document.getElementById('locateBtn');
    const origText = btn.innerHTML;
    btn.innerHTML = '⏳ Locating...';
    btn.disabled = true;

    try {
      // Fetch IP-based location as fallback
      const ipRes = await fetch('https://api.bigdatacloud.net/data/reverse-geocode-client');
      const ipData = await ipRes.json();
      
      const success = async (pos) => {
        const lat = pos.coords.latitude;
        const lon = pos.coords.longitude;
        const res = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`);
        const data = await res.json();
        const zip = data.address.postcode;
        const ccode = data.address.country_code;
        if(zip && ccode) {
           window.location.href = 'pages/' + ccode.toLowerCase() + '.html?q=' + encodeURIComponent(zip);
        } else if (ipData && ipData.postcode && ipData.countryCode) {
           window.location.href = 'pages/' + ipData.countryCode.toLowerCase() + '.html?q=' + encodeURIComponent(ipData.postcode);
        } else {
           alert('Could not detect postal code for your location.');
           btn.innerHTML = origText;
           btn.disabled = false;
        }
      };

      const error = () => {
        if (ipData && ipData.postcode && ipData.countryCode) {
           window.location.href = 'pages/' + ipData.countryCode.toLowerCase() + '.html?q=' + encodeURIComponent(ipData.postcode);
        } else {
           alert('Location permission denied or failed, and IP fallback failed.');
           btn.innerHTML = origText;
           btn.disabled = false;
        }
      };

      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success, error, {timeout: 10000});
      } else {
        error();
      }
    } catch(e) {
      alert('Network error while locating.');
      btn.innerHTML = origText;
      btn.disabled = false;
    }
  }
</script>
'''

html = html.replace('</script>\n</body>', js_function + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
