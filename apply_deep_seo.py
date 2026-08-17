import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Title and H1 alignment
# Current Title: PO ZipCode Global — Find Postal Codes for 121 Countries
# We will set Title to: Global Postal Code & ZIP Code Finder | PO ZipCode Global
content = re.sub(r'<title>.*?</title>', '<title>Global Postal Code & ZIP Code Finder | PO ZipCode Global</title>', content)

# Remove old Open Graph tags and insert new comprehensive ones
content = re.sub(r'<meta property="og:.*?>', '', content)
og_tags = '''
<meta property="og:title" content="Global Postal Code & ZIP Code Finder | PO ZipCode Global">
<meta property="og:description" content="Find any PIN Code or Postal Code worldwide. An interactive directory for shipping and mailing in 121+ countries.">
<meta property="og:image" content="https://pozip.me/home/assets/social-preview.jpg">
<meta property="og:url" content="https://pozip.me/">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
'''
content = content.replace('</title>', '</title>\n' + og_tags)

# Enhanced Schema: Organization + Article + BreadcrumbList + FAQPage
schema_json = '''
<!-- Comprehensive SEO Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://pozip.me/#website",
      "url": "https://pozip.me/",
      "name": "PO ZipCode Global",
      "description": "Find postal codes and zip codes for 121+ countries."
    },
    {
      "@type": "Organization",
      "@id": "https://pozip.me/#organization",
      "name": "PO ZipCode Global",
      "url": "https://pozip.me/",
      "logo": "https://pozip.me/home/assets/logo.png",
      "sameAs": ["https://github.com/chaitanyadev999/zipcode-global"]
    },
    {
      "@type": "Article",
      "@id": "https://pozip.me/#article",
      "isPartOf": {"@id": "https://pozip.me/#website"},
      "headline": "Global Postal Code & ZIP Code Finder",
      "description": "A complete guide and tool to finding postal codes, ZIP codes, and PIN codes for over 121 countries.",
      "author": {"@id": "https://pozip.me/#organization"},
      "publisher": {"@id": "https://pozip.me/#organization"},
      "datePublished": "2026-08-01T08:00:00+00:00",
      "dateModified": "2026-08-17T12:00:00+00:00"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://pozip.me/"
      }]
    }
  ]
}
</script>
'''
if 'Comprehensive SEO Schema' not in content:
    content = content.replace('</head>', schema_json + '\n</head>')

# Ensure we remove any old schema block that might conflict
content = re.sub(r'<!-- Structured Data -->.*?</script>', '', content, flags=re.DOTALL)

# Top Summary & Definition Support & Audience Clarity (GEO/AEO)
hero_replacement = '''<h1>Global Postal Code & ZIP Code Finder</h1>
<div class="top-summary" style="max-width: 800px; margin: 1rem auto; padding: 1.5rem; background: var(--bg-veil); border-left: 4px solid var(--cyan); text-align: left; border-radius: var(--r-md);">
  <strong>What is a Postal Code?</strong> A postal code (also known as a ZIP code or PIN code) is a sequence of letters and numbers added to a postal address to route mail efficiently. 
  <br><br>
  <strong>Who is this for?</strong> This tool is designed for logistics professionals, international shoppers, developers, and everyday users who need to verify mailing addresses or calculate shipping zones.
  <br><br>
  <strong>Key Takeaway:</strong> You can instantly look up accurate postal codes for over 121 countries using our interactive database and live maps, updated as of <time datetime="2026-08-17">August 17, 2026</time> by the <span itemprop="author">PO ZipCode Global Team</span>.
</div>'''
# Replace the H1 area
content = re.sub(r'<h1>.*?</h1>', hero_replacement, content, count=1, flags=re.DOTALL)
# Remove old top summary if it exists
content = re.sub(r'<p class="hero-desc".*?</p>', '', content, count=1, flags=re.DOTALL)

# Remove the old FAQ section if I added it previously so I don't duplicate
content = re.sub(r'<!-- FAQ Section for SEO -->.*?</section>', '', content, flags=re.DOTALL)

# Detailed AEO/GEO FAQ Section with External Source and Steps
new_faq_section = '''
<!-- FAQ Section for SEO -->
<section style="max-width: 800px; margin: 4rem auto; padding: 0 1rem; text-align: left;">
  <h2 style="font-size: 2rem; margin-bottom: 2rem; color: var(--cyan); border-bottom: 1px solid var(--border-light); padding-bottom: 0.5rem;">Frequently Asked Questions & Guide</h2>
  
  <article style="margin-bottom: 2.5rem;">
    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">How to find a ZIP code or Postal code online?</h3>
    <p style="margin-bottom: 1rem; color: var(--t2);">Finding your postal code online is simple. Follow these 3 easy steps using our tool:</p>
    <ol style="margin-left: 2rem; margin-bottom: 1rem; color: var(--t2); line-height: 1.8;">
      <li><strong>Select your country:</strong> Choose from over 121 supported countries in the global dropdown.</li>
      <li><strong>Pick your state and city:</strong> Narrow down your region to load the precise districts.</li>
      <li><strong>View on the interactive map:</strong> The exact postal code and boundaries will appear on the map instantly.</li>
    </ol>
    <p style="color: var(--t2);">This method ensures you get the most accurate, real-time data for shipping and mailing.</p>
  </article>

  <article style="margin-bottom: 2.5rem;">
    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Why are postal codes important for shipping?</h3>
    <p style="color: var(--t2); line-height: 1.6;">Postal codes are essential for the automated sorting of mail and packages. Without a correct postal code, your delivery might be severely delayed or returned to the sender. According to credible sources like <a href="https://en.wikipedia.org/wiki/Postal_code" target="_blank" rel="noopener noreferrer" style="color:var(--cyan); text-decoration:underline;">Wikipedia's Postal Code guide</a>, modern logistics networks rely entirely on these standardized codes to calculate shipping rates and determine optimal delivery routes.</p>
  </article>
</section>
'''
if 'Frequently Asked Questions & Guide' not in content:
    content = content.replace('</main>', new_faq_section + '\n</main>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Deep SEO/AEO/GEO updates applied to index.html')
