import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Favicon and Open Graph tags
favicon_og = '''
<!-- Favicon -->
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🌍</text></svg>">
<!-- Open Graph -->
<meta property="og:title" content="PO ZipCode Global — Find Postal Codes for 121 Countries">
<meta property="og:description" content="Find any PIN Code or Postal Code around the world. Browse states, cities, and districts with an interactive live map.">
<meta property="og:image" content="https://pozip.me/home/assets/social-preview.jpg">
<meta property="og:url" content="https://pozip.me/">
<meta property="og:type" content="website">
'''
if 'property="og:title"' not in content:
    content = content.replace('</title>', '</title>\n' + favicon_og)

# 2. Add Schema tags (WebSite, Organization, FAQPage)
schema_tags = '''
<!-- Structured Data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "url": "https://pozip.me/",
      "name": "PO ZipCode Global",
      "description": "Find postal codes and zip codes for 121 countries.",
      "publisher": {
        "@type": "Organization",
        "name": "PO ZipCode Global",
        "url": "https://pozip.me/",
        "logo": "https://pozip.me/home/assets/logo.png"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "What is a postal code?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A postal code (also known as a PIN code or ZIP code) is a series of letters or digits appended to a postal address for the purpose of sorting mail."
        }
      }, {
        "@type": "Question",
        "name": "How do I find my zip code?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "You can use our Instant Finder tool on PO ZipCode Global. Simply select your country, state, and city to instantly see the correct postal code on an interactive map."
        }
      }]
    }
  ]
}
</script>
'''
if 'application/ld+json' not in content:
    content = content.replace('</head>', schema_tags + '\n</head>')

# 3. Update H1 and add Top Summary and Author
h1_replacement = '''<h1>Global Postal Code & Zip Code Finder</h1>
<p class="hero-desc" style="max-width: 600px; margin: 1rem auto; font-size: 1.1rem; line-height: 1.6;">
  <strong>PO ZipCode Global</strong> is your ultimate tool for finding accurate postal codes across 121 countries. 
  Whether for shipping, mailing, or address verification, our interactive map makes it easy.
  <br><br>
  <span style="font-size: 0.85rem; opacity: 0.8;">Last Updated: August 2026 &middot; By the PO ZipCode Global Data Team &middot; Data sourced from <a href="https://github.com/chaitanyadev999/zipcode-global" target="_blank" style="color:var(--cyan);text-decoration:none;">Official Repositories</a></span>
</p>'''

content = re.sub(r'<h1>PO ZipCode Global</h1>\s*<p class="hero-desc">Find any PIN Code.*?</p>', h1_replacement, content, flags=re.DOTALL)

# 4. Add an FAQ section (H2) for SEO structure
faq_section = '''
<!-- FAQ Section for SEO -->
<section style="max-width: 800px; margin: 4rem auto; padding: 0 1rem; text-align: left;">
  <h2 style="font-size: 2rem; margin-bottom: 2rem; color: var(--cyan); text-align: center;">Frequently Asked Questions</h2>
  
  <div style="margin-bottom: 2rem; background: var(--card-bg); padding: 1.5rem; border-radius: var(--r-lg); border: 1px solid var(--border-light);">
    <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">What is a postal code?</h3>
    <p style="color: var(--t2); line-height: 1.6;">A postal code (often called a PIN code in India, or ZIP code in the US) is a unique sequence of numbers or letters added to a postal address. It helps local postal services route and sort mail efficiently. Having the correct postal code ensures your packages and letters arrive on time without getting lost.</p>
  </div>
  
  <div style="margin-bottom: 2rem; background: var(--card-bg); padding: 1.5rem; border-radius: var(--r-lg); border: 1px solid var(--border-light);">
    <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">How do I find my zip code or PIN code?</h3>
    <p style="color: var(--t2); line-height: 1.6;">Using <strong>PO ZipCode Global</strong>, you can quickly find your postal code by using the Instant Finder at the top of this page. Simply select your <em>Country</em>, followed by your <em>State/Province</em>, and then your <em>City/District</em>. Our system will instantly display the correct code along with a live interactive map.</p>
  </div>
</section>
'''
if 'Frequently Asked Questions' not in content:
    content = content.replace('</main>', faq_section + '\n</main>')

# 5. Fix img alt tags
# We will just replace alt="" with alt="Country Flag"
content = content.replace('alt=""', 'alt="Country flag icon"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('SEO fixes applied to index.html')
