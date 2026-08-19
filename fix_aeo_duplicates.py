import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Title to align with H1
content = re.sub(r'<title>.*?</title>', '<title>Find Postal & ZIP Codes for 121+ Countries | PO ZipCode Global</title>', content, count=1)
content = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Find Postal & ZIP Codes for 121+ Countries | PO ZipCode Global">', content, count=1)

# 2. Clean ALL badly injected FAQ items
bad_faq_pattern = r'<div style="margin-bottom: 2\.5rem; background: var\(--card-bg\); padding: 1\.5rem; border-radius: var\(--r-md\); border: 1px solid var\(--border-hi\);">\s*<h3 style="font-size: 1\.5rem; margin-bottom: 1rem;">ZIP Code vs PIN Code vs Postal Code: What\'s the difference\?</h3>\s*<p style="color: var\(--t2\); line-height: 1\.6;">.*?</p>\s*</div>'
content = re.sub(bad_faq_pattern, '', content, flags=re.DOTALL)

# 3. Clean old top-summary if it accidentally got left behind anywhere
content = re.sub(r'<!-- AEO / GEO Top Summary -->\s*<div class="top-summary".*?</div>', '', content, flags=re.DOTALL)

# 4. Inject Top Summary Answer right before INSTANT FINDER FORM
top_summary = '''
<!-- AEO / GEO Top Summary -->
<div class="top-summary" style="max-width: 900px; margin: 0 auto 3rem auto; padding: 1.5rem; background: rgba(10,14,39,0.8); border-left: 4px solid var(--cyan); text-align: left; border-radius: var(--r-md); box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
  <p style="color: var(--t2); margin-bottom: 0.5rem; font-size: 1rem;"><strong>What is a Postal Code?</strong> A postal code (also known as a ZIP code or PIN code) is a sequence of letters and numbers added to a postal address to route mail efficiently.</p>
  <p style="color: var(--t2); margin-bottom: 0.5rem; font-size: 1rem;"><strong>Who is this for?</strong> This tool is designed for logistics professionals, international shoppers, developers, and everyday users who need to verify mailing addresses or calculate shipping zones.</p>
  <p style="color: var(--t2); font-size: 1rem;"><strong>Key Takeaway:</strong> You can instantly look up accurate postal codes for over 121 countries using our interactive database and live maps, updated as of <time datetime="2026-08-17">August 17, 2026</time> by the <span itemprop="author">PO ZipCode Global Team</span>.</p>
</div>
'''
if '<!-- AEO / GEO Top Summary -->' not in content:
    content = content.replace('<!-- INSTANT FINDER FORM -->', top_summary + '\n<!-- INSTANT FINDER FORM -->')

# 5. Inject the extra FAQ item correctly into the FAQ section (right before </main>)
# First, find the Frequently Asked Questions & Guide section
faq_extra = '''
  <div style="margin-bottom: 2.5rem; background: var(--card-bg); padding: 1.5rem; border-radius: var(--r-md); border: 1px solid var(--border-hi);">
    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">ZIP Code vs PIN Code vs Postal Code: What's the difference?</h3>
    <p style="color: var(--t2); line-height: 1.6;">They all serve the exact same purpose, but are used in different regions. <strong>ZIP Code</strong> (Zone Improvement Plan) is specifically used in the United States. For example, a famous ZIP code is Beverly Hills, <strong>90210</strong>. <strong>PIN Code</strong> (Postal Index Number) is used in India, such as New Delhi's <strong>110001</strong>. Meanwhile, most of the world simply calls it a <strong>Postal Code</strong> or Postcode.</p>
  </div>
'''

if 'ZIP Code vs PIN Code vs Postal Code' not in content:
    # Inject right before </main>
    # Check if FAQ section exists near </main>
    content = content.replace('</section>\n</main>', faq_extra + '\n</section>\n</main>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Cleaned duplicates, fixed title, injected top summary and added single FAQ item.')
