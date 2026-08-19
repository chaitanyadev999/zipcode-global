import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Restore the Hero H1 and Paragraph
hero_correct = '''<h1>Find <span class="grad-text">Postal & ZIP Codes</span> for 121+ Countries</h1>
<p class="hero-desc">Search instant PIN codes, ZIP codes and Postcodes worldwide. Includes complete states, cities, districts, interactive maps & full location details.</p>'''

# Replace my ugly H1 and top-summary with the correct hero text
content = re.sub(r'<h1>Global Postal Code & ZIP Code Finder</h1>\s*<div class="top-summary".*?</div>', hero_correct, content, flags=re.DOTALL)

# 2. Inject Top Summary Below the Hero Search Box
# We'll put it right after the stats section or before it. Let's look for the closing div of the search section.
# Actually, let's put it right after <div class="features-grid">
top_summary_seo = '''
<!-- AEO / GEO Top Summary -->
<div class="top-summary" style="max-width: 1000px; margin: 3rem auto; padding: 2rem; background: var(--card-bg); border-left: 4px solid var(--cyan); text-align: left; border-radius: var(--r-md); box-shadow: var(--shadow-md);">
  <h2 style="font-size: 1.4rem; margin-bottom: 0.5rem;">Global Postal Code & ZIP Code Finder</h2>
  <p style="color: var(--t2); margin-bottom: 0.5rem;"><strong>What is a Postal Code?</strong> A postal code (also known as a ZIP code or PIN code) is a sequence of letters and numbers added to a postal address to route mail efficiently.</p>
  <p style="color: var(--t2); margin-bottom: 0.5rem;"><strong>Who is this for?</strong> This tool is designed for logistics professionals, international shoppers, developers, and everyday users who need to verify mailing addresses or calculate shipping zones.</p>
  <p style="color: var(--t2);"><strong>Key Takeaway:</strong> You can instantly look up accurate postal codes for over 121 countries using our interactive database and live maps, updated as of <time datetime="2026-08-17">August 17, 2026</time> by the <span itemprop="author">PO ZipCode Global Team</span>.</p>
</div>
'''
if 'AEO / GEO Top Summary' not in content:
    content = content.replace('<div class="features-grid">', top_summary_seo + '\n<div class="features-grid">')

# 3. Add FAQ Section right before <footer>
new_faq_section = '''
<!-- FAQ Section for SEO -->
<section style="max-width: 1000px; margin: 4rem auto; padding: 0 1rem; text-align: left;">
  <h2 style="font-size: 2rem; margin-bottom: 2rem; color: var(--cyan); border-bottom: 1px solid var(--border-light); padding-bottom: 0.5rem;">Frequently Asked Questions & Guide</h2>
  
  <article style="margin-bottom: 2.5rem; background: var(--card-bg); padding: 1.5rem; border-radius: var(--r-md); border: 1px solid var(--border-hi);">
    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">How to find a ZIP code or Postal code online?</h3>
    <p style="margin-bottom: 1rem; color: var(--t2);">Finding your postal code online is simple. Follow these 3 easy steps using our tool:</p>
    <ol style="margin-left: 2rem; margin-bottom: 1rem; color: var(--t2); line-height: 1.8;">
      <li><strong>Select your country:</strong> Choose from over 121 supported countries in the global dropdown.</li>
      <li><strong>Pick your state and city:</strong> Narrow down your region to load the precise districts.</li>
      <li><strong>View on the interactive map:</strong> The exact postal code and boundaries will appear on the map instantly.</li>
    </ol>
    <p style="color: var(--t2);">This method ensures you get the most accurate, real-time data for shipping and mailing.</p>
  </article>

  <article style="margin-bottom: 2.5rem; background: var(--card-bg); padding: 1.5rem; border-radius: var(--r-md); border: 1px solid var(--border-hi);">
    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Why are postal codes important for shipping?</h3>
    <p style="color: var(--t2); line-height: 1.6;">Postal codes are essential for the automated sorting of mail and packages. Without a correct postal code, your delivery might be severely delayed or returned to the sender. According to credible sources like <a href="https://en.wikipedia.org/wiki/Postal_code" target="_blank" rel="noopener noreferrer" style="color:var(--cyan); text-decoration:underline;">Wikipedia's Postal Code guide</a>, modern logistics networks rely entirely on these standardized codes to calculate shipping rates and determine optimal delivery routes.</p>
  </article>
</section>
'''
if 'Frequently Asked Questions & Guide' not in content:
    content = content.replace('<footer>', new_faq_section + '\n<footer>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Restored hero text and correctly injected deep SEO.')
