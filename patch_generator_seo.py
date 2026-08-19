import os

def patch_generator():
    file_path = 'generate_pages.py'
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Inject sr-only summary
    target_h1 = '<h1><span class="grad">{{NAME}}</span> {{TERM}} Directory</h1>'
    replacement_h1 = '''<h1><span class="grad">{{NAME}}</span> {{TERM}} Directory</h1>
  <!-- SEO Hidden Summaries (Screen Reader Only) -->
  <div style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;">
    <strong>Top Summary:</strong> The ultimate directory to instantly verify and search accurate postal codes, ZIP codes, and PIN codes for {{NAME}} and 121+ countries worldwide.
    <strong>Bottom Line:</strong> Get instant access to millions of {{TERM}}s in {{NAME}} updated live.
  </div>'''

    if target_h1 in text and '<!-- SEO Hidden Summaries' not in text:
        text = text.replace(target_h1, replacement_h1)
        print('Injected sr-only summary')

    # 2. Inject Audience, FAQ, and Key Takeaways
    target_footer = '<footer>'
    replacement_footer = '''<!-- SEO Sections -->
<div class="sec">
  <section class="use-case-section" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 212, 255, 0.1); border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem;">
    <h2 style="font-family: var(--fd); font-size: 1.25rem; color: var(--p); margin-bottom: 1rem;">Target Audience, Use Cases & Industry Context for {{NAME}}</h2>
    <p style="font-size: 0.9rem; line-height: 1.6; color: var(--t2); margin-bottom: 1rem;">
      Whether you are an e-commerce business shipping packages to <strong>{{NAME}}</strong>, a data analyst validating user addresses, or a local resident sending mail, having the correct <strong>{{TERM}}</strong> is essential. Postal and ZIP codes ensure accurate logistics, prevent delivery delays, and help businesses segment regional data.
    </p>
    <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.5rem;">Who uses this {{TERM}} directory?</h3>
    <ul style="font-size: 0.9rem; color: var(--t2); line-height: 1.6; padding-left: 1.2rem; margin-bottom: 1rem;">
      <li><strong>E-commerce & Retail:</strong> For validating shipping addresses during checkout.</li>
      <li><strong>Logistics & Delivery:</strong> Couriers routing packages efficiently across states and cities.</li>
      <li><strong>Data Entry & Verification:</strong> Securing accurate geographic data for KYC and onboarding.</li>
      <li><strong>General Public:</strong> Finding local post offices and specific {{TERM}}s for personal mail.</li>
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

  <section class="faq-section" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 212, 255, 0.1); border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem;">
    <h2 style="font-family: var(--fd); font-size: 1.25rem; color: var(--p); margin-bottom: 1rem;">Frequently Asked Questions (FAQ)</h2>
    
    <div style="margin-bottom: 1rem;">
      <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.3rem;">1. How do I find my {{TERM}} in {{NAME}}?</h3>
      <p style="font-size: 0.9rem; color: var(--t2);">You can easily find your {{TERM}} by searching your city, district, or state using the search bar above. Our interactive map also allows you to explore codes geographically.</p>
    </div>
    
    <div style="margin-bottom: 1rem;">
      <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.3rem;">2. Are the {{TERM}}s in this directory accurate?</h3>
      <p style="font-size: 0.9rem; color: var(--t2);">Yes, our database is regularly updated and synced with official postal data to ensure high accuracy for logistics, mail, and address validation.</p>
    </div>
    
    <div>
      <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.3rem;">3. What is the difference between a ZIP code and a Postal Code?</h3>
      <p style="font-size: 0.9rem; color: var(--t2);">A ZIP code is specifically used in the United States, while a Postal Code is the generic term used internationally. In {{NAME}}, the official term is {{TERM}}.</p>
    </div>
  </section>

  <div style="background: rgba(124, 58, 237, 0.1); border-left: 4px solid var(--a); padding: 1rem; border-radius: 0 8px 8px 0; margin-bottom: 2rem;">
    <h3 style="font-size: 1rem; color: var(--t); margin-bottom: 0.5rem;">Key Takeaways</h3>
    <p style="font-size: 0.9rem; color: var(--t2); line-height: 1.5; margin: 0;">
      Always use the correct <strong>{{TERM}}</strong> for {{NAME}} to avoid mail delays. Our platform provides free, instant access to over 121+ countries' postal data, ensuring you have the right information for global shipping and validation.
    </p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do I find my {{TERM}} in {{NAME}}?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "You can easily find your {{TERM}} by searching your city, district, or state using the search bar above. Our interactive map also allows you to explore codes geographically."
    }
  }, {
    "@type": "Question",
    "name": "Are the {{TERM}}s in this directory accurate?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes, our database is regularly updated and synced with official postal data to ensure high accuracy for logistics, mail, and address validation."
    }
  }, {
    "@type": "Question",
    "name": "What is the difference between a ZIP code and a Postal Code?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "A ZIP code is specifically used in the United States, while a Postal Code is the generic term used internationally. In {{NAME}}, the official term is {{TERM}}."
    }
  }]
}
</script>

<footer>'''

    if target_footer in text and 'Target Audience, Use Cases' not in text:
        # replace the LAST occurrence of <footer> to be safe
        text = text.replace(target_footer, replacement_footer, 1)
        print('Injected bottom SEO sections')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('generate_pages.py patched successfully.')

if __name__ == '__main__':
    patch_generator()
