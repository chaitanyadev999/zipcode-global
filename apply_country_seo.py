import glob
import re
import os

for filepath in glob.glob('pages/*.html'):
    if 'template' in filepath: continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract current Title
    m = re.search(r'<title>(.*?)</title>', content)
    page_title = m.group(1) if m else 'PO ZipCode Global'
    country_name = page_title.split('—')[0].strip() if '—' in page_title else page_title

    # 1. Open Graph
    if 'og:title' not in content:
        og_tags = f'''
<meta property="og:title" content="{page_title}">
<meta property="og:description" content="Find postal codes, ZIP codes, and PIN codes for {country_name}. Explore all states, cities, and regions with an interactive map.">
<meta property="og:image" content="https://pozip.me/home/assets/social-preview.jpg">
<meta property="og:type" content="article">
'''
        content = content.replace('</title>', '</title>\n' + og_tags)

    # 2. Schema Injection (Article + Breadcrumb)
    schema_id = filepath.replace('pages\\\\', '').replace('pages/', '').replace('.html', '')
    url = f"https://pozip.me/pages/{schema_id}.html"
    
    schema_json = f'''
<!-- Deep SEO Schema -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://pozip.me/"}},
        {{"@type": "ListItem", "position": 2, "name": "{country_name}", "item": "{url}"}}
      ]
    }},
    {{
      "@type": "Article",
      "headline": "Postal Codes and ZIP Codes in {country_name}",
      "description": "Comprehensive postal code directory for {country_name}.",
      "author": {{"@type": "Organization", "name": "PO ZipCode Global", "url": "https://pozip.me/"}},
      "publisher": {{"@type": "Organization", "name": "PO ZipCode Global", "logo": "https://pozip.me/home/assets/logo.png"}},
      "mainEntityOfPage": "{url}",
      "datePublished": "2026-08-01T08:00:00+00:00",
      "dateModified": "2026-08-17T12:00:00+00:00"
    }}
  ]
}}
</script>
'''
    if 'Deep SEO Schema' not in content:
        content = content.replace('</head>', schema_json + '\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied Deep SEO Schema and OpenGraph to all 120 country pages!")
