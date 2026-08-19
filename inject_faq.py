import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

faq_extra = '''
  <div style="margin-bottom: 2.5rem; background: var(--card-bg); padding: 1.5rem; border-radius: var(--r-md); border: 1px solid var(--border-hi);">
    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">ZIP Code vs PIN Code vs Postal Code: What's the difference?</h3>
    <p style="color: var(--t2); line-height: 1.6;">They all serve the exact same purpose, but are used in different regions. <strong>ZIP Code</strong> (Zone Improvement Plan) is specifically used in the United States. For example, a famous ZIP code is Beverly Hills, <strong>90210</strong>. <strong>PIN Code</strong> (Postal Index Number) is used in India, such as New Delhi's <strong>110001</strong>. Meanwhile, most of the world simply calls it a <strong>Postal Code</strong> or Postcode.</p>
  </div>
'''

content = re.sub(r'</section>\s*</main>', faq_extra + '\n</section>\n</main>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Added single FAQ item successfully.')
