with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'function findMyLocation' not in html:
    html = html.replace('</body>', '''
<script>
  async function findMyLocation() {
    const btn = document.getElementById('locateBtn');
    if (!btn) return;
    const origText = btn.innerHTML;
    btn.innerHTML = '⏳ Locating...';
    btn.disabled = true;

    try {
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
      if(btn) {
        btn.innerHTML = origText;
        btn.disabled = false;
      }
    }
  }
</script>
</body>''')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
