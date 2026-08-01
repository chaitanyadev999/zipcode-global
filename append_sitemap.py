import os
sitemap_txt = r'C:\Users\recla\zipcode-global\sitemap_cities.txt'
sitemap_xml = r'C:\Users\recla\zipcode-global\sitemap.xml'

with open(sitemap_xml, 'r', encoding='utf-8') as f:
    xml = f.read()

urls = ''
if os.path.exists(sitemap_txt):
    with open(sitemap_txt, 'r', encoding='utf-8') as f:
        content = f.read()
    # It might be separated by literal \n
    lines = content.split('\\n')
    if len(lines) == 1:
        lines = content.split('\n')
        
    for l in lines:
        if l.strip() and f'<loc>{l.strip()}</loc>' not in xml:
            urls += f'  <url>\n    <loc>{l.strip()}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.64</priority>\n  </url>\n'

xml = xml.replace('</urlset>', urls + '</urlset>')

with open(sitemap_xml, 'w', encoding='utf-8') as f:
    f.write(xml)
print(f'Appended {urls.count("<url>")} URLs to sitemap.xml')
