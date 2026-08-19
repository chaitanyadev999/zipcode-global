import os

filepath = 'pages/shared_pseo.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace initPage() logic to hide statesSection on PSEO pages
old_code = """
    // Stats
    $('heroStats').innerHTML =
      '<div class="stat"><span class="stat-num">' + COUNTRY.states.length + '</span><span class="stat-label">Regions</span></div>' +
      '<div class="stat"><span class="stat-num">' + COUNTRY.code + '</span><span class="stat-label">Country Code</span></div>' +
      '<div class="stat"><span class="stat-num">' + META.region + '</span><span class="stat-label">Continent</span></div>';

    renderStates();
  }
"""

new_code = """
    // Stats
    $('heroStats').innerHTML =
      '<div class="stat"><span class="stat-num">' + COUNTRY.states.length + '</span><span class="stat-label">Regions</span></div>' +
      '<div class="stat"><span class="stat-num">' + COUNTRY.code + '</span><span class="stat-label">Country Code</span></div>' +
      '<div class="stat"><span class="stat-num">' + META.region + '</span><span class="stat-label">Continent</span></div>';

    if (window.PSEO_CITY || window.PSEO_IS_STATE) {
      if ($('statesSection')) $('statesSection').style.display = 'none';
    } else {
      renderStates();
    }
  }
"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched initPage successfully!")
else:
    print("Could not find old_code in shared_pseo.js")
