with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# 1. Remove the first Key Takeaway box above the search bar
start_box = text.find('<div class="summary-box"')
end_box = text.find('</div>', start_box) + 6
if start_box != -1 and 'Key Takeaway' in text[start_box:end_box]:
    text = text[:start_box] + text[end_box:]
    print('Removed top summary box')

# 2. Update the Audience section to include specific keywords
old_use_case = '''<section class="use-case-section" style="max-width: 1200px; margin: 40px auto; padding: 0 15px;">
  <h2 style="font-size: 2rem; margin-bottom: 1.5rem; color: var(--cyan); border-bottom: 1px solid var(--border-light); padding-bottom: 0.5rem;">Who is this directory for?</h2>
  <p style="font-size: 1.1rem; color: #ccc; margin-bottom: 1.5rem; line-height: 1.6;">Our global postal code directory is designed for a diverse audience with varying needs:</p>
  <ul style="list-style-type: disc; margin-left: 20px; color: #ccc; font-size: 1.1rem; line-height: 1.6;">
    <li><strong>E-commerce Businesses:</strong> Validate shipping addresses and calculate accurate delivery rates.</li>
    <li><strong>Logistics & Couriers:</strong> Ensure precise package routing and minimize delivery errors.</li>
    <li><strong>Frequent Travelers & Expats:</strong> Easily find local postal codes for visa applications or new residencies.</li>
    <li><strong>Data Analysts:</strong> Access structured location data for demographic research and mapping.</li>
  </ul>
</section>'''

new_use_case = '''<section class="use-case-section" style="max-width: 1200px; margin: 40px auto; padding: 0 15px;">
  <h2 style="font-size: 2rem; margin-bottom: 1.5rem; color: var(--cyan); border-bottom: 1px solid var(--border-light); padding-bottom: 0.5rem;">Target Audience, Use Cases & Industry Context</h2>
  <p style="font-size: 1.1rem; color: #ccc; margin-bottom: 1.5rem; line-height: 1.6;">Our global postal code directory is designed for a diverse <strong>audience</strong> across multiple <strong>industries</strong>. Here are the primary <strong>use cases</strong> and the <strong>decision context</strong> for using our tool:</p>
  <ul style="list-style-type: disc; margin-left: 20px; color: #ccc; font-size: 1.1rem; line-height: 1.6;">
    <li><strong>E-commerce Industry (Use Case):</strong> Validate shipping addresses at checkout to make accurate shipping pricing decisions.</li>
    <li><strong>Logistics & Couriers (Audience):</strong> Ensure precise package routing and minimize delivery errors in an international context.</li>
    <li><strong>Travelers & Expats:</strong> Find local postal codes for visa applications or residency documentation.</li>
    <li><strong>Data Analysts:</strong> Access structured location data to drive demographic research and business decisions.</li>
  </ul>
</section>'''

if old_use_case in text:
    text = text.replace(old_use_case, new_use_case)
    print('Updated Audience section')
else:
    print('Audience section not found!')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
