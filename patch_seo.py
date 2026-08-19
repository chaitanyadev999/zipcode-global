import os

filepath = 'index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

modified = False

# 1. Heading structure (H3 to H2)
old_h3 = '<h3 style="color:var(--t); font-size:1.4rem; margin-bottom:0.5rem; text-align:center;">⚡ Instant ZIP Code Finder</h3>'
new_h2 = '<h2 style="color:var(--t); font-size:1.4rem; margin-bottom:0.5rem; text-align:center;">⚡ Instant ZIP Code Finder</h2>'
if old_h3 in content:
    content = content.replace(old_h3, new_h2)
    modified = True

# 2. Top Summary Answer
hero_desc = '<p class="hero-desc">Search instant PIN codes, ZIP codes and Postcodes worldwide. Includes complete states, cities, districts, interactive maps & full location details.</p>'
summary_box = """
<div class="summary-box" style="background: rgba(0, 212, 255, 0.1); border-left: 4px solid var(--cyan); padding: 15px; margin: 20px auto; max-width: 800px; text-align: left; border-radius: 4px;">
  <strong style="color:#fff;">Key Takeaway:</strong> <span style="color:#ccc;">A postal code (ZIP code, PIN code, or postcode) is a series of letters or digits appended to a postal address for the purpose of sorting mail. PO ZipCode Global provides instant, up-to-date access to over 50 million postal codes across 121+ countries.</span>
</div>
"""
if hero_desc in content and 'summary-box' not in content:
    content = content.replace(hero_desc, hero_desc + '\n' + summary_box)
    modified = True

# 3. Audience & Table
faq_header = '<h2 style="font-size: 2rem; margin-bottom: 2rem; color: var(--cyan); border-bottom: 1px solid var(--border-light); padding-bottom: 0.5rem;">Frequently Asked Questions & Guide</h2>'
audience_and_table = """
<section class="use-case-section" style="max-width: 1200px; margin: 40px auto; padding: 0 15px;">
  <h2 style="font-size: 2rem; margin-bottom: 1.5rem; color: var(--cyan); border-bottom: 1px solid var(--border-light); padding-bottom: 0.5rem;">Who is this directory for?</h2>
  <p style="font-size: 1.1rem; color: #ccc; margin-bottom: 1.5rem; line-height: 1.6;">Our global postal code directory is designed for a diverse audience with varying needs:</p>
  <ul style="list-style-type: disc; margin-left: 20px; color: #ccc; font-size: 1.1rem; line-height: 1.6;">
    <li><strong>E-commerce Businesses:</strong> Validate shipping addresses and calculate accurate delivery rates.</li>
    <li><strong>Logistics & Couriers:</strong> Ensure precise package routing and minimize delivery errors.</li>
    <li><strong>Frequent Travelers & Expats:</strong> Easily find local postal codes for visa applications or new residencies.</li>
    <li><strong>Data Analysts:</strong> Access structured location data for demographic research and mapping.</li>
  </ul>
</section>

<section class="deep-coverage-section" style="max-width: 1200px; margin: 40px auto; padding: 0 15px;">
  <h2 style="font-size: 2rem; margin-bottom: 1.5rem; color: var(--cyan); border-bottom: 1px solid var(--border-light); padding-bottom: 0.5rem;">Postal Code Terminology Worldwide</h2>
  <p style="font-size: 1.1rem; color: #ccc; margin-bottom: 1.5rem; line-height: 1.6;">Different countries use different terminologies and formats for their postal routing systems. Here is a quick comparison of the most common formats:</p>
  
  <div style="overflow-x:auto;">
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 2rem; color: #fff; background: rgba(255,255,255,0.05); border-radius: 8px;">
      <thead>
        <tr style="background: rgba(0, 212, 255, 0.2);">
          <th style="padding: 12px; border: 1px solid var(--border-light); text-align: left;">Term</th>
          <th style="padding: 12px; border: 1px solid var(--border-light); text-align: left;">Countries Used In</th>
          <th style="padding: 12px; border: 1px solid var(--border-light); text-align: left;">Format Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding: 12px; border: 1px solid var(--border-light);">ZIP Code</td>
          <td style="padding: 12px; border: 1px solid var(--border-light);">United States, Philippines</td>
          <td style="padding: 12px; border: 1px solid var(--border-light);">90210 or 90210-1234</td>
        </tr>
        <tr>
          <td style="padding: 12px; border: 1px solid var(--border-light);">PIN Code</td>
          <td style="padding: 12px; border: 1px solid var(--border-light);">India</td>
          <td style="padding: 12px; border: 1px solid var(--border-light);">110001 (6 digits)</td>
        </tr>
        <tr>
          <td style="padding: 12px; border: 1px solid var(--border-light);">Postcode</td>
          <td style="padding: 12px; border: 1px solid var(--border-light);">United Kingdom, Australia</td>
          <td style="padding: 12px; border: 1px solid var(--border-light);">SW1A 1AA or 2000</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

"""
if faq_header in content and 'use-case-section' not in content:
    content = content.replace(faq_header, audience_and_table + faq_header)
    modified = True

# 4. FAQ Schema
faq_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How to find a ZIP code or Postal code online?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Finding your postal code online is simple. Follow these 3 easy steps using our tool: 1. Select your country. 2. Pick your state and city. 3. View on the interactive map."
      }
    },
    {
      "@type": "Question",
      "name": "Why are postal codes important for shipping?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Postal codes are essential for the automated sorting of mail and packages. Without a correct postal code, your delivery might be severely delayed or returned."
      }
    },
    {
      "@type": "Question",
      "name": "ZIP Code vs PIN Code vs Postal Code: What's the difference?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They all serve the same purpose but are used in different countries. ZIP Code is used in the US, PIN Code is used in India, and Postal Code is the internationally recognized term."
      }
    }
  ]
}
</script>
"""
if 'FAQPage' not in content:
    content = content.replace('</body>', faq_schema + '\n</body>')
    modified = True

if modified:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched index.html successfully!")
else:
    print("No changes made to index.html")
