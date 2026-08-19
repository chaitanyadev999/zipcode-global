import os
import glob
import re
import datetime
import multiprocessing

NEW_HEAD_META_TEMPLATE = """<meta name="description" content="Looking for {CITY}, {STATE} {TERM}s? Get instant access to accurate postal data, complete directory, and geographic details for {CITY}, {COUNTRY}.">
<link rel="canonical" href="https://pozip.me/{PATH_URL}" />
<meta property="og:title" content="{CITY} {TERM}s, {STATE}, {COUNTRY} | PO ZipCode Global" />
<meta property="og:description" content="Looking for {CITY}, {STATE} {TERM}s? Get instant access to accurate postal data, complete directory, and geographic details for {CITY}, {COUNTRY}." />
<meta property="og:url" content="https://pozip.me/{PATH_URL}" />
<meta property="og:type" content="website" />"""

NEW_BOTTOM_BLOCK_TEMPLATE = """<!-- SEO Sections for {CITY} -->
<details class="seo-text" style="padding: 20px; background: rgba(255,255,255,0.05); margin: 20px auto; max-width: 800px; border-radius: 8px; color: #ccc; line-height: 1.6; text-align: center; font-size: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); cursor: pointer;">
  <summary style="font-size: 1.1rem; color: #00d4ff; font-weight: bold; text-align: left; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; outline: none; list-style: none;">
    Read More About {CITY} {TERM}s & SEO Data ▾
  </summary>
  <div style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;">
    <strong>Top Summary:</strong> The ultimate directory to instantly verify and search accurate postal codes, ZIP codes, and PIN codes for {CITY}, {STATE} and 121+ countries worldwide.
    <strong>Bottom Line:</strong> Get instant access to millions of {TERM}s in {CITY} updated live.
  </div>

  <section class="use-case-section" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 212, 255, 0.1); border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem; text-align: left; font-size: 1rem;">
    <h2 style="font-family: var(--fd, sans-serif); font-size: 1.25rem; color: #fff; margin-bottom: 1rem;">Target Audience, Use Cases & Industry Context for {CITY}</h2>
    <p style="font-size: 0.9rem; line-height: 1.6; color: #aaa; margin-bottom: 1rem;">
      Whether you are an e-commerce business shipping packages to <strong>{CITY}, {STATE}</strong>, a data analyst validating user addresses, or a local resident sending mail, having the correct <strong>{TERM}</strong> is essential. Postal and ZIP codes ensure accurate logistics, prevent delivery delays, and help businesses segment regional data.
    </p>
    <h3 style="font-size: 1rem; color: #ddd; margin-bottom: 0.5rem;">Who uses this {TERM} directory in {CITY}?</h3>
    <ul style="font-size: 0.9rem; color: #aaa; line-height: 1.6; padding-left: 1.2rem; margin-bottom: 1rem;">
      <li><strong>E-commerce & Retail:</strong> For validating shipping addresses during checkout.</li>
      <li><strong>Logistics & Delivery:</strong> Couriers routing packages efficiently across states and cities.</li>
      <li><strong>Data Entry & Verification:</strong> Securing accurate geographic data for KYC and onboarding.</li>
      <li><strong>General Public:</strong> Finding local post offices and specific {TERM}s for personal mail.</li>
    </ul>
    
    <h3 style="font-size: 1rem; color: #ddd; margin-bottom: 0.5rem;">Postal Code vs ZIP Code vs PIN Code</h3>
    <div style="overflow-x: auto; margin-bottom: 1rem;">
      <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem; text-align: left; color: #aaa;">
        <thead>
          <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <th style="padding: 8px;">Terminology</th>
            <th style="padding: 8px;">Meaning</th>
            <th style="padding: 8px;">Primary Usage</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
            <td style="padding: 8px; color: #ddd;"><strong>Postal Code</strong></td>
            <td style="padding: 8px;">Alphanumeric or numeric code for mail sorting.</td>
            <td style="padding: 8px;">Global standard (UK, Canada, Europe, etc.)</td>
          </tr>
          <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
            <td style="padding: 8px; color: #ddd;"><strong>ZIP Code</strong></td>
            <td style="padding: 8px;">Zone Improvement Plan (numeric).</td>
            <td style="padding: 8px;">Primarily United States (USPS).</td>
          </tr>
          <tr>
            <td style="padding: 8px; color: #ddd;"><strong>PIN Code</strong></td>
            <td style="padding: 8px;">Postal Index Number (6-digit numeric).</td>
            <td style="padding: 8px;">India (India Post).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="faq-section" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 212, 255, 0.1); border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem; text-align: left;">
    <h2 style="font-family: var(--fd, sans-serif); font-size: 1.25rem; color: #fff; margin-bottom: 1rem;">Frequently Asked Questions (FAQ)</h2>
    
    <div style="margin-bottom: 1rem;">
      <h3 style="font-size: 1rem; color: #ddd; margin-bottom: 0.3rem;">1. How do I find my {TERM} in {CITY}?</h3>
      <p style="font-size: 0.9rem; color: #aaa;">You can easily find your {TERM} by searching your city, district, or state using the search bar above. Our interactive map also allows you to explore codes geographically.</p>
    </div>
    
    <div style="margin-bottom: 1rem;">
      <h3 style="font-size: 1rem; color: #ddd; margin-bottom: 0.3rem;">2. Are the {TERM}s in this directory accurate?</h3>
      <p style="font-size: 0.9rem; color: #aaa;">Yes, our database is regularly updated and synced with official postal data to ensure high accuracy for logistics, mail, and address validation. Verified against local postal databases.</p>
    </div>
    
    <div>
      <h3 style="font-size: 1rem; color: #ddd; margin-bottom: 0.3rem;">3. What is the difference between a ZIP code and a Postal Code?</h3>
      <p style="font-size: 0.9rem; color: #aaa;">A ZIP code is specifically used in the United States, while a Postal Code is the generic term used internationally. The official term used here is {TERM}.</p>
    </div>
  </section>

  <div style="background: rgba(124, 58, 237, 0.1); border-left: 4px solid #7c3aed; padding: 1rem; border-radius: 0 8px 8px 0; margin-bottom: 2rem; text-align: left;">
    <h3 style="font-size: 1rem; color: #ddd; margin-bottom: 0.5rem;">Key Takeaways</h3>
    <p style="font-size: 0.9rem; color: #aaa; line-height: 1.5; margin: 0;">
      Always use the correct <strong>{TERM}</strong> for {CITY} to avoid mail delays. Our platform provides free, instant access to over 121+ countries' postal data, ensuring you have the right information for global shipping and validation.
    </p>
  </div>
</details>

<script type="application/ld+json">
[
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{CITY} {TERM} Directory",
    "description": "Looking for {CITY}, {STATE} {TERM}s? Get instant access to accurate postal data, complete directory, and geographic details for {CITY}, {COUNTRY}.",
    "url": "https://pozip.me/{PATH_URL}",
    "publisher": {{
      "@type": "Organization",
      "name": "PO ZipCode Global",
      "url": "https://pozip.me",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://pozip.me/home/assets/logo.png"
      }}
    }}
  }},
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://pozip.me/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{COUNTRY}",
        "item": "https://pozip.me/pages/{COUNTRY_PATH}.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{STATE}",
        "item": "https://pozip.me/pages/{COUNTRY_PATH}/{STATE_PATH}.html"
      }},
      {{
        "@type": "ListItem",
        "position": 4,
        "name": "{CITY}"
      }}
    ]
  }},
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "How do I find my {TERM} in {CITY}?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "You can easily find your {TERM} by searching your city, district, or state using the search bar above. Our interactive map also allows you to explore codes geographically."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Are the {TERM}s in this directory accurate?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes, our database is regularly updated and synced with official postal data to ensure high accuracy for logistics, mail, and address validation. Verified against local postal databases."
        }}
      }},
      {{
        "@type": "Question",
        "name": "What is the difference between a ZIP code and a Postal Code?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "A ZIP code is specifically used in the United States, while a Postal Code is the generic term used internationally. The official term used here is {TERM}."
        }}
      }}
    ]
  }}
]
</script>"""

def process_file(file_path):
    if file_path.endswith('about.html') or file_path.endswith('main.html'):
        return 0, 1
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        if '<details class="seo-text"' in text:
            return 0, 1
            
        city_match = re.search(r'window\.PSEO_CITY="([^"]+)";', text)
        state_match = re.search(r'window\.PSEO_STATE_LABEL="([^"]+)";', text)
        if not state_match:
            state_match = re.search(r'window\.PSEO_STATE="([^"]+)";', text)
        term_match = re.search(r'window\.PSEO_TERM="([^"]+)";', text)
        country_match = re.search(r'window\.PSEO_COUNTRY="([^"]+)";', text)
        
        if not city_match or not state_match or not country_match:
            if 'PSEO_IS_STATE=true' in text:
                city_match = state_match
            else:
                return 0, 1
                
        city_name = city_match.group(1)
        state_name = state_match.group(1).replace('.json', '')
        country_code = country_match.group(1).upper()
        
        path_parts = file_path.replace('\\\\', '/').replace('\\', '/').split('/')
        country_path = path_parts[1] if len(path_parts) > 1 else ''
        state_path = path_parts[2].replace('.html', '') if len(path_parts) == 3 else (path_parts[2] if len(path_parts) > 2 else '')
        path_url = file_path.replace('\\\\', '/').replace('\\', '/')
        
        term_name = "Postal Code"
        if term_match:
            term_name = term_match.group(1)
        else:
            if country_code == 'IN': term_name = 'PIN Code'
            elif country_code == 'US': term_name = 'ZIP Code'
            elif country_code == 'GB' or country_code == 'UK': term_name = 'Postcode'
        
        country_name = "Country"
        title_match = re.search(r'<title>.*?,\s*([^,]+)\s*\|\s*PO ZipCode Global</title>', text)
        if title_match:
            country_name = title_match.group(1).strip()
        else:
            if country_code == 'IN': country_name = 'India'
            elif country_code == 'US': country_name = 'United States'
            elif country_code == 'CA': country_name = 'Canada'
        
        # 1. Replace the old schema block at the top if it exists
        text = re.sub(r'<script type="application/ld\+json">\s*\\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"WebPage".*?</script>', '', text, flags=re.DOTALL)
        
        # 2. Replace the Meta Description and add OG/Canonical tags
        head_meta = NEW_HEAD_META_TEMPLATE.format(CITY=city_name, STATE=state_name, TERM=term_name, COUNTRY=country_name, PATH_URL=path_url)
        text = re.sub(r'<meta name="description" content="[^"]*">', head_meta, text, count=1)
        
        # 3. Replace the old bottom SEO block
        start_idx = text.find('<!-- SEO Sections for')
        if start_idx != -1:
            end_idx = text.find('<script src=', start_idx)
            if end_idx != -1:
                bottom_block = NEW_BOTTOM_BLOCK_TEMPLATE.format(
                    CITY=city_name, STATE=state_name, TERM=term_name, COUNTRY=country_name, 
                    PATH_URL=path_url, COUNTRY_PATH=country_path, STATE_PATH=state_path
                )
                text = text[:start_idx] + bottom_block + '\\n\\n' + text[end_idx:]
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                return 1, 0
    except Exception as e:
        return 0, 1
    return 0, 0

if __name__ == '__main__':
    # Fix multiprocessing on Windows
    multiprocessing.freeze_support()
    
    print("Collecting files...", flush=True)
    files = glob.glob('pages/*/*/*.html') + glob.glob('pages/*/*.html')
    files = [f for f in files if '\\pages\\' not in f]
    print(f"Total files found: {len(files)}", flush=True)
    
    # Process files in parallel
    pool = multiprocessing.Pool(processes=min(multiprocessing.cpu_count(), 16))
    results = pool.imap_unordered(process_file, files, chunksize=100)
    
    total_patched = 0
    total_skipped = 0
    processed_count = 0
    
    for patched, skipped in results:
        total_patched += patched
        total_skipped += skipped
        processed_count += 1
        
        if processed_count % 5000 == 0:
            print(f"Processed {processed_count}/{len(files)} files... (Patched: {total_patched}, Skipped: {total_skipped})", flush=True)
            
    pool.close()
    pool.join()
    
    print(f"DONE! Total Patched: {total_patched}, Total Skipped: {total_skipped}", flush=True)
