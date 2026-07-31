import os

template_file = r'C:\Users\recla\zipcode-global\pages\country-template.html'

with open(template_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_render = """    $('resultsList').innerHTML = results.map((item, idx) => {
      const pin = item.pincode || item.ZipCode || item.zipcode || 'N/A';
      const office = item.officename || item.OfficeName || item.City || 'Location';
      const state = item.statename || item.State || '';
      const district = item.district || item.County || item.City || '';
      const region = item.regionname || item.Country || '';
      const division = item.divisionname || '';
      const delivery = item.delivery || '';
      const hasCoords = item.latitude != null && item.longitude != null;
      return '<div class="result-card" style="animation-delay:' + idx * 50 + 'ms">' +
        '<div class="result-pin"><span class="result-pin-num">' + pin + '</span><button class="copy-btn" data-pin="' + pin + '">📋</button></div>' +
        '<div class="result-office">' + office + '</div>' +
        '<div class="result-meta">' +
          '<div class="meta-item"><span class="meta-label">State</span><span class="meta-value">' + (state || 'N/A') + '</span></div>' +
          '<div class="meta-item"><span class="meta-label">District</span><span class="meta-value">' + (district || 'N/A') + '</span></div>' +
          '<div class="meta-item"><span class="meta-label">Region</span><span class="meta-value">' + (region || 'N/A') + '</span></div>' +
          '<div class="meta-item"><span class="meta-label">Division</span><span class="meta-value">' + (division || 'N/A') + '</span></div>' +
        '</div>' +"""

new_render = """    $('resultsList').innerHTML = results.map((item, idx) => {
      let stateLbl = 'State';
      let distLbl = 'District';
      if (['US','GB','IE'].includes(C.code)) distLbl = 'County';
      else if (C.code === 'JP') { stateLbl = 'Prefecture'; distLbl = 'City/Ward'; }
      else if (C.code === 'CA') { stateLbl = 'Province'; distLbl = 'County/City'; }
      else if (C.code === 'CN') { stateLbl = 'Province'; distLbl = 'Prefecture'; }
      else if (C.code === 'FR') { stateLbl = 'Region'; distLbl = 'Department'; }
      else if (C.code === 'IT') { stateLbl = 'Region'; distLbl = 'Province'; }
      else if (C.code === 'ES') { stateLbl = 'Community'; distLbl = 'Province'; }
      else if (C.code === 'AU') { stateLbl = 'State'; distLbl = 'Region'; }
      else if (C.code === 'BR') { stateLbl = 'State'; distLbl = 'Municipality'; }
      else if (C.code === 'ZA') { stateLbl = 'Province'; distLbl = 'Municipality'; }
      else if (C.code === 'RU') { stateLbl = 'Republic/Oblast'; distLbl = 'District'; }
      else if (C.code !== 'IN') { stateLbl = 'Province/State'; distLbl = 'County/City'; }

      const pin = item.pincode || item.ZipCode || item.zipcode || 'N/A';
      const office = item.officename || item.OfficeName || item.City || 'Location';
      const state = item.statename || item.State || '';
      const district = item.district || item.County || item.City || '';
      const region = item.regionname || item.Country || '';
      const division = item.divisionname || '';
      const delivery = item.delivery || '';
      const hasCoords = item.latitude != null && item.longitude != null;
      return '<div class="result-card" style="animation-delay:' + idx * 50 + 'ms">' +
        '<div class="result-pin"><span class="result-pin-num">' + pin + '</span><button class="copy-btn" data-pin="' + pin + '">📋</button></div>' +
        '<div class="result-office">' + office + '</div>' +
        '<div class="result-meta">' +
          '<div class="meta-item"><span class="meta-label">' + stateLbl + '</span><span class="meta-value">' + (state || 'N/A') + '</span></div>' +
          '<div class="meta-item"><span class="meta-label">' + distLbl + '</span><span class="meta-value">' + (district || 'N/A') + '</span></div>' +
          '<div class="meta-item"><span class="meta-label">Region</span><span class="meta-value">' + (region || 'N/A') + '</span></div>' +
          '<div class="meta-item"><span class="meta-label">Division</span><span class="meta-value">' + (division || 'N/A') + '</span></div>' +
        '</div>' +"""

if old_render in content:
    content = content.replace(old_render, new_render)
    with open(template_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully patched renderResults in country-template.html")
else:
    print("Could not find the exact text in country-template.html!")
