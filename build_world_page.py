import json, re

# Read COUNTRY_DB from shared_pseo.js
with open('pages/shared_pseo.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const COUNTRY_DB = (\{.*?\n\s*\});', text, re.DOTALL)
js_obj = m.group(1)

# Quick parse of js_obj to dict
# Replace keys without quotes
import ast
# Let's parse with regex
countries = []
for line in js_obj.splitlines():
    match = re.search(r"'([A-Z]{2})':\{name:'(.*?)',lat:(.*?),lon:(.*?),region:'(.*?)'\}", line)
    if match:
        code, name, lat, lon, region = match.groups()
        # Determine URL
        c_lower = code.lower()
        if c_lower == 'in':
            href = '/pages/india.html'
        elif c_lower == 'us':
            href = '/pages/usa.html'
        else:
            href = f'/pages/{c_lower}.html'
        countries.append({
            'code': code,
            'name': name,
            'region': region,
            'href': href,
            'flag': f'https://flagcdn.com/w80/{c_lower}.png'
        })

print(f'Parsed {len(countries)} countries')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Global Postal Code Directory — All 121 Countries | PO ZipCode Global</title>
  <meta name="description" content="Explore the comprehensive global directory of postal codes, ZIP codes, and PIN codes across 121 countries. Search and browse locations worldwide."/>
  <link rel="canonical" href="https://pozip.me/pages/world.html"/>
  <link rel="icon" type="image/png" href="/home/assets/logo.png">

  <!-- Open Graph -->
  <meta property="og:type" content="website"/>
  <meta property="og:title" content="Global Postal Code Directory — All 121 Countries"/>
  <meta property="og:description" content="Explore the world's complete postal code directory covering 121 countries and 180,000+ regions."/>
  <meta property="og:url" content="https://pozip.me/pages/world.html"/>
  <meta property="og:image" content="https://pozip.me/home/assets/social-preview.jpg"/>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;600&display=optional" rel="stylesheet">

  <style>
    :root {{
      --bg: #050816;
      --bg-card: rgba(255, 255, 255, 0.04);
      --bg-card-hi: rgba(255, 255, 255, 0.08);
      --border: rgba(0, 212, 255, 0.15);
      --border-hi: rgba(0, 212, 255, 0.4);
      --cyan: #00d4ff;
      --purple: #7c3aed;
      --text: #f0f2f8;
      --text-dim: #94a3b8;
      --font-main: 'Inter', sans-serif;
      --font-display: 'Space Grotesk', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --grad: linear-gradient(135deg, #00d4ff 0%, #7c3aed 100%);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: var(--font-main);
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      overflow-x: hidden;
    }}
    body::before {{
      content: '';
      position: fixed; inset: 0; z-index: -1;
      background: radial-gradient(circle at 50% 10%, rgba(0, 212, 255, 0.08) 0%, transparent 60%),
                  radial-gradient(circle at 80% 80%, rgba(124, 58, 237, 0.08) 0%, transparent 50%);
    }}
    /* NAV */
    .nav {{
      display: flex; justify-content: space-between; align-items: center;
      padding: 1rem 2rem; border-bottom: 1px solid var(--border);
      background: rgba(5, 8, 22, 0.85); backdrop-filter: blur(20px);
      position: sticky; top: 0; z-index: 100;
    }}
    .nav-brand {{ display: flex; align-items: center; gap: 0.8rem; text-decoration: none; color: #fff; font-weight: 700; font-family: var(--font-display); }}
    .nav-brand img {{ width: 34px; height: 34px; border-radius: 8px; }}
    .nav-links {{ display: flex; align-items: center; gap: 0.8rem; }}
    .nav-btn {{
      padding: 0.5rem 1rem; border-radius: 999px; text-decoration: none; color: var(--text-dim);
      font-size: 0.85rem; font-weight: 600; border: 1px solid var(--border);
      background: var(--bg-card); transition: all 0.25s ease;
    }}
    .nav-btn:hover {{ color: #fff; border-color: var(--cyan); background: var(--bg-card-hi); }}
    .nav-btn.active {{ color: #000; background: var(--grad); border-color: transparent; }}

    /* HERO */
    .hero {{ text-align: center; padding: 3.5rem 1.5rem 2rem; max-width: 900px; margin: 0 auto; }}
    .hero-badge {{
      display: inline-flex; align-items: center; gap: 0.5rem;
      padding: 0.4rem 1rem; border-radius: 999px; font-size: 0.8rem;
      font-family: var(--font-mono); color: var(--cyan);
      background: rgba(0, 212, 255, 0.1); border: 1px solid var(--border);
      margin-bottom: 1.2rem;
    }}
    .hero h1 {{
      font-family: var(--font-display); font-size: clamp(2rem, 5vw, 3.2rem);
      font-weight: 800; line-height: 1.15; margin-bottom: 1rem;
      background: linear-gradient(135deg, #fff 40%, var(--cyan) 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    .hero p {{ color: var(--text-dim); font-size: 1.05rem; line-height: 1.6; max-width: 650px; margin: 0 auto 2rem; }}

    /* SEARCH & FILTER */
    .search-wrap {{ max-width: 600px; margin: 0 auto 2rem; position: relative; }}
    .search-input {{
      width: 100%; padding: 0.9rem 1.4rem; border-radius: 999px;
      background: var(--bg-card); border: 1px solid var(--border);
      color: #fff; font-size: 1rem; font-family: var(--font-main);
      outline: none; transition: all 0.25s ease;
    }}
    .search-input:focus {{ border-color: var(--cyan); box-shadow: 0 0 25px rgba(0, 212, 255, 0.25); }}

    .filter-pills {{ display: flex; justify-content: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 2.5rem; }}
    .pill {{
      padding: 0.45rem 1.1rem; border-radius: 999px; border: 1px solid var(--border);
      background: var(--bg-card); color: var(--text-dim); font-size: 0.85rem; font-weight: 600;
      cursor: pointer; transition: all 0.2s ease;
    }}
    .pill:hover {{ color: #fff; border-color: var(--cyan); }}
    .pill.active {{ background: var(--grad); color: #000; border-color: transparent; }}

    /* GRID */
    .grid {{
      display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1.25rem; max-width: 1250px; margin: 0 auto; padding: 0 1.5rem 4rem;
    }}
    .country-card {{
      display: flex; align-items: center; gap: 1rem;
      padding: 1rem 1.2rem; border-radius: 14px;
      background: var(--bg-card); border: 1px solid var(--border);
      text-decoration: none; color: inherit; transition: all 0.25s ease;
    }}
    .country-card:hover {{
      transform: translateY(-3px); border-color: var(--cyan);
      background: var(--bg-card-hi); box-shadow: 0 8px 30px rgba(0, 212, 255, 0.15);
    }}
    .country-flag {{
      width: 44px; height: 32px; object-fit: cover; border-radius: 6px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.4);
    }}
    .country-info h3 {{ font-size: 1rem; font-weight: 700; color: #fff; margin-bottom: 0.2rem; }}
    .country-info span {{ font-size: 0.78rem; color: var(--cyan); font-family: var(--font-mono); text-transform: uppercase; }}

    /* FOOTER */
    footer {{ border-top: 1px solid var(--border); padding: 2.5rem 1.5rem; text-align: center; color: var(--text-dim); font-size: 0.88rem; }}
    .footer-links {{ display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 1rem; flex-wrap: wrap; }}
    .footer-links a {{ color: var(--text-dim); text-decoration: none; transition: color 0.2s; }}
    .footer-links a:hover {{ color: var(--cyan); }}

    @media(max-width: 768px) {{
      .nav {{ padding: 0.8rem 1rem; flex-direction: column; gap: 0.8rem; }}
      .nav-links {{ width: 100%; overflow-x: auto; justify-content: center; padding-bottom: 0.3rem; }}
      .grid {{ grid-template-columns: 1fr; }}
    }}
  </style>

  <!-- Schema.org -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "Global Postal Code Directory — All 121 Countries",
    "description": "Comprehensive directory of postal codes and ZIP codes for 121 countries across 6 continents.",
    "url": "https://pozip.me/pages/world.html",
    "creator": {{
      "@type": "Organization",
      "name": "PO ZipCode Global",
      "url": "https://pozip.me/"
    }},
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "mainEntity": {{
      "@type": "Dataset",
      "name": "Global Postal Code Database",
      "description": "Worldwide postal code, ZIP code, and PIN code datasets covering 121 countries and 180,000+ cities.",
      "creator": {{
        "@type": "Organization",
        "name": "PO ZipCode Global",
        "url": "https://pozip.me/"
      }},
      "license": "https://creativecommons.org/licenses/by/4.0/"
    }}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://pozip.me/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Global Directory", "item": "https://pozip.me/pages/world.html" }}
    ]
  }}
  </script>
</head>
<body>

  <nav class="nav">
    <a href="/" class="nav-brand">
      <img src="/home/assets/logo.png" alt="PO ZipCode Global Logo">
      <span>PO ZipCode Global</span>
    </a>
    <div class="nav-links">
      <a href="/" class="nav-btn">🏠 Home</a>
      <a href="/pages/world.html" class="nav-btn active">🌍 All 121 Countries</a>
      <a href="/postal-code-of-my-location.html" class="nav-btn">📍 Find My Location</a>
      <a href="/pages/about.html" class="nav-btn">About</a>
    </div>
  </nav>

  <header class="hero">
    <div class="hero-badge">🌍 GLOBAL POSTAL DIRECTORY</div>
    <h1>Browse Postal Codes by Country</h1>
    <p>Access official postal codes, ZIP codes, and PIN codes across all 121 supported countries and 180,000+ cities worldwide.</p>

    <div class="search-wrap">
      <input type="text" id="filterSearch" class="search-input" placeholder="Type a country name or code..." oninput="doSearch()"/>
    </div>

    <div class="filter-pills">
      <button class="pill active" onclick="setContinent('all', this)">All (121)</button>
      <button class="pill" onclick="setContinent('Asia', this)">Asia</button>
      <button class="pill" onclick="setContinent('Europe', this)">Europe</button>
      <button class="pill" onclick="setContinent('Americas', this)">Americas</button>
      <button class="pill" onclick="setContinent('Oceania', this)">Oceania</button>
      <button class="pill" onclick="setContinent('Africa', this)">Africa</button>
    </div>
  </header>

  <main class="grid" id="countryGrid">
'''

for c in sorted(countries, key=lambda x: x['name']):
    html_content += f'''    <a href="{c['href']}" class="country-card" data-name="{c['name'].lower()}" data-code="{c['code'].lower()}" data-region="{c['region']}">
      <img src="{c['flag']}" alt="{c['name']} flag" class="country-flag" loading="lazy">
      <div class="country-info">
        <h3>{c['name']}</h3>
        <span>{c['region']} • {c['code']}</span>
      </div>
    </a>\n'''

html_content += '''  </main>

  <footer>
    <div class="footer-links">
      <a href="/">Home</a>
      <a href="/pages/world.html">Global Directory</a>
      <a href="/postal-code-of-my-location.html">Postal Code of My Location</a>
      <a href="/pages/about.html">About</a>
      <a href="/pages/privacy.html">Privacy</a>
      <a href="/pages/report.html">Report Issue</a>
    </div>
    <p>© 2026 PO ZipCode Global. All rights reserved. Fast, accurate, global postal search.</p>
  </footer>

  <script>
    let activeRegion = 'all';

    function setContinent(region, btn) {
      activeRegion = region;
      document.querySelectorAll('.pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterGrid();
    }

    function doSearch() {
      filterGrid();
    }

    function filterGrid() {
      const q = document.getElementById('filterSearch').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.country-card');

      cards.forEach(card => {
        const name = card.getAttribute('data-name');
        const code = card.getAttribute('data-code');
        const region = card.getAttribute('data-region');

        const matchesRegion = (activeRegion === 'all' || region === activeRegion);
        const matchesQuery = (!q || name.includes(q) || code.includes(q));

        if (matchesRegion && matchesQuery) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
'''

with open('pages/world.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Successfully generated pages/world.html')
