import os
import re

pages_dir = r"C:\Users\recla\zipcode-global\pages"

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    filename = os.path.basename(filepath)
    country_name = filename.replace('.html', '').replace('-', ' ').title()

    # 1. Remove the previously injected block that was put right before </body>
    if '<div id="seo-content-injected"' in content:
        # We know it was placed right at the end of the body
        pattern = r'<div id="seo-content-injected".*?</div>\s*</body>'
        # We need re.DOTALL so .*? matches newlines
        content = re.sub(pattern, '</body>', content, flags=re.DOTALL)
    
    # 2. Inject it BEFORE <footer>
    # Let's check if we still need to inject it (i.e. it's not already before footer)
    if 'id="seo-content-injected"' not in content:
        seo_visible_text = f'''
<div id="seo-content-injected" style="max-width: 960px; margin: 2rem auto; padding: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1); color: var(--t2); font-size: 0.85rem; line-height: 1.6;">
  <h2 style="font-size: 1.1rem; color: var(--p); margin-bottom: 1rem;">About {country_name} Postal Codes</h2>
  <p><strong>Definition:</strong> A PIN code (Postal Index Number) or ZIP code in {country_name} is a numerical or alphanumeric code used by the postal service to route mail efficiently to specific states, cities, and districts.</p>
  <p><strong>Examples of Postal Formats:</strong> Different regions may use different formats. For example, India uses a 6-digit PIN code system, while the USA uses a 5-digit ZIP code system. Always verify the correct format for your specific delivery address in {country_name}.</p>
  <p><strong>Key Benefits of our Directory:</strong></p>
  <ul style="margin-left: 1.5rem; margin-bottom: 1rem;">
    <li>Accurate and up-to-date postal data for {country_name}.</li>
    <li>Interactive maps for geographical verification.</li>
    <li>Complete coverage of all states and districts.</li>
  </ul>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "PO ZipCode Global",
    "url": "https://pozip.me/",
    "logo": "https://pozip.me/assets/logo.png",
    "sameAs": [
      "https://twitter.com/pozipcode",
      "https://facebook.com/pozipcode"
    ]
  }}
  </script>
</div>
'''
        footer_idx = content.find('<footer>')
        if footer_idx != -1:
            content = content[:footer_idx] + seo_visible_text + content[footer_idx:]

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for file in os.listdir(pages_dir):
    if file.endswith('.html'):
        filepath = os.path.join(pages_dir, file)
        if os.path.isfile(filepath):
            if patch_file(filepath):
                count += 1

print(f"Repatched {count} country files successfully.")
