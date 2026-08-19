import os
import glob
import re

SEO_TEMPLATE = """<!-- SEO Sections for {CITY} -->
<div class="seo-text">
  <div style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;">
    <strong>Top Summary:</strong> The ultimate directory to instantly verify and search accurate postal codes, ZIP codes, and PIN codes for {CITY}, {STATE} and 121+ countries worldwide.
    <strong>Bottom Line:</strong> Get instant access to millions of {TERM}s in {CITY} updated live.
  </div>

  <section class="use-case-section" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 212, 255, 0.1); border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem; text-align: left; font-size: 1rem;">
    <h2 style="font-family: var(--fd); font-size: 1.25rem; color: var(--p); margin-bottom: 1rem;">Target Audience, Use Cases & Industry Context for {CITY}</h2>
    <p style="font-size: 0.9rem; line-height: 1.6; color: var(--t2); margin-bottom: 1rem;">
      Whether you are an e-commerce business shipping packages to <strong>{CITY}, {STATE}</strong>, a data analyst validating user addresses, or a local resident sending mail, having the correct <strong>{TERM}</strong> is essential. Postal and ZIP codes ensure accurate logistics, prevent delivery delays, and help businesses segment regional data.
    </p>
    <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.5rem;">Who uses this {TERM} directory in {CITY}?</h3>
    <ul style="font-size: 0.9rem; color: var(--t2); line-height: 1.6; padding-left: 1.2rem; margin-bottom: 1rem;">
      <li><strong>E-commerce & Retail:</strong> For validating shipping addresses during checkout.</li>
      <li><strong>Logistics & Delivery:</strong> Couriers routing packages efficiently across states and cities.</li>
      <li><strong>Data Entry & Verification:</strong> Securing accurate geographic data for KYC and onboarding.</li>
      <li><strong>General Public:</strong> Finding local post offices and specific {TERM}s for personal mail.</li>
    </ul>
    
    <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.5rem;">Postal Code vs ZIP Code vs PIN Code</h3>
    <div style="overflow-x: auto; margin-bottom: 1rem;">
      <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem; text-align: left; color: var(--t2);">
        <thead>
          <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <th style="padding: 8px;">Terminology</th>
            <th style="padding: 8px;">Meaning</th>
            <th style="padding: 8px;">Primary Usage</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
            <td style="padding: 8px; color: var(--t);"><strong>Postal Code</strong></td>
            <td style="padding: 8px;">Alphanumeric or numeric code for mail sorting.</td>
            <td style="padding: 8px;">Global standard (UK, Canada, Europe, etc.)</td>
          </tr>
          <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
            <td style="padding: 8px; color: var(--t);"><strong>ZIP Code</strong></td>
            <td style="padding: 8px;">Zone Improvement Plan (numeric).</td>
            <td style="padding: 8px;">Primarily United States (USPS).</td>
          </tr>
          <tr>
            <td style="padding: 8px; color: var(--t);"><strong>PIN Code</strong></td>
            <td style="padding: 8px;">Postal Index Number (6-digit numeric).</td>
            <td style="padding: 8px;">India (India Post).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="faq-section" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 212, 255, 0.1); border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem; text-align: left;">
    <h2 style="font-family: var(--fd); font-size: 1.25rem; color: var(--p); margin-bottom: 1rem;">Frequently Asked Questions (FAQ)</h2>
    
    <div style="margin-bottom: 1rem;">
      <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.3rem;">1. How do I find my {TERM} in {CITY}?</h3>
      <p style="font-size: 0.9rem; color: var(--t2);">You can easily find your {TERM} by searching your city, district, or state using the search bar above. Our interactive map also allows you to explore codes geographically.</p>
    </div>
    
    <div style="margin-bottom: 1rem;">
      <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.3rem;">2. Are the {TERM}s in this directory accurate?</h3>
      <p style="font-size: 0.9rem; color: var(--t2);">Yes, our database is regularly updated and synced with official postal data to ensure high accuracy for logistics, mail, and address validation.</p>
    </div>
    
    <div>
      <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.3rem;">3. What is the difference between a ZIP code and a Postal Code?</h3>
      <p style="font-size: 0.9rem; color: var(--t2);">A ZIP code is specifically used in the United States, while a Postal Code is the generic term used internationally. The official term used here is {TERM}.</p>
    </div>
  </section>

  <div style="background: rgba(124, 58, 237, 0.1); border-left: 4px solid var(--a); padding: 1rem; border-radius: 0 8px 8px 0; margin-bottom: 2rem; text-align: left;">
    <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.5rem;">Key Takeaways</h3>
    <p style="font-size: 0.9rem; color: var(--t2); line-height: 1.5; margin: 0;">
      Always use the correct <strong>{TERM}</strong> for {CITY} to avoid mail delays. Our platform provides free, instant access to over 121+ countries' postal data, ensuring you have the right information for global shipping and validation.
    </p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{{
    "@type": "Question",
    "name": "How do I find my {TERM} in {CITY}?",
    "acceptedAnswer": {{
      "@type": "Answer",
      "text": "You can easily find your {TERM} by searching your city, district, or state using the search bar above. Our interactive map also allows you to explore codes geographically."
    }}
  }}, {{
    "@type": "Question",
    "name": "Are the {TERM}s in this directory accurate?",
    "acceptedAnswer": {{
      "@type": "Answer",
      "text": "Yes, our database is regularly updated and synced with official postal data to ensure high accuracy for logistics, mail, and address validation."
    }}
  }}, {{
    "@type": "Question",
    "name": "What is the difference between a ZIP code and a Postal Code?",
    "acceptedAnswer": {{
      "@type": "Answer",
      "text": "A ZIP code is specifically used in the United States, while a Postal Code is the generic term used internationally."
    }}
  }}]
}}
</script>"""

def patch_city_pages():
    files = glob.glob('pages/*/*/*.html') + glob.glob('pages/*/*.html')
    # Filter out actual country pages which are in pages/ (we already did those)
    files = [f for f in files if '\\pages\\' not in f]
    # Actually glob handles relative properly, but we only want depth 2 and 3: pages/IN/ap.html and pages/IN/ap/vizag.html
    # Country pages are pages/india.html so they are depth 1. We're safe.
    
    count = 0
    for file_path in files:
        if file_path.endswith('about.html') or file_path.endswith('main.html'):
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        if 'Target Audience, Use Cases' in text:
            continue # already patched
            
        # Extract variables using regex or simple find
        try:
            city_match = re.search(r'window\.PSEO_CITY="([^"]+)";', text)
            state_match = re.search(r'window\.PSEO_STATE_LABEL="([^"]+)";', text)
            if not state_match:
                state_match = re.search(r'window\.PSEO_STATE="([^"]+)";', text)
            term_match = re.search(r'window\.PSEO_TERM="([^"]+)";', text)
            
            if not city_match or not state_match or not term_match:
                # Might be a state page, let's check
                if 'PSEO_IS_STATE=true' in text:
                    city_match = state_match # For state pages, the "City" context is the State itself
                else:
                    continue
                    
            city_name = city_match.group(1)
            state_name = state_match.group(1).replace('.json', '')
            term_name = term_match.group(1)
            
            seo_block = SEO_TEMPLATE.format(CITY=city_name, STATE=state_name, TERM=term_name)
            
            # Replace the old <div class="seo-text">...</div> with the new one
            # The old one might span multiple lines
            start_idx = text.find('<div class="seo-text">')
            end_idx = text.find('</div>', start_idx)
            
            if start_idx != -1 and end_idx != -1:
                # Need to also find where to inject the script schema
                text_to_replace = text[start_idx:end_idx+6]
                text = text.replace(text_to_replace, seo_block)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                count += 1
        except Exception as e:
            print(f"Error on {file_path}: {e}")
            
    print(f"Patched {count} city/state pages successfully.")

if __name__ == '__main__':
    patch_city_pages()
