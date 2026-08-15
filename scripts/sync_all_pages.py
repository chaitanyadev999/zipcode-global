import os
import re

# 1. Read the new script block from country-template.html
template_path = r"C:\Users\recla\zipcode-global\pages\country-template.html"
with open(template_path, 'r', encoding='utf-8') as f:
    template_html = f.read()

script_marker = "// ── HAND-CRAFTED UNIQUE FLAG THEME COLORS FOR ALL 121 COUNTRIES"
end_marker = "})();\n</script>"

start_idx = template_html.find(script_marker)
end_idx = template_html.find(end_marker) + len(end_marker) - 9 # exclude </script>
if start_idx == -1 or end_idx < start_idx:
    print("Error finding script block in template")
    exit(1)

new_script = template_html[start_idx:end_idx]

# 2. Read the new nav block from main.html
main_path = r"C:\Users\recla\zipcode-global\home\main.html"
with open(main_path, 'r', encoding='utf-8') as f:
    main_html = f.read()

nav_match = re.search(r'<nav class="nav"[^>]*>.*?</nav>', main_html, re.DOTALL)
if not nav_match:
    print("Error finding nav block in main.html")
    exit(1)

new_nav = nav_match.group(0)

# Replace the specific 'href="/#countriesSection"' with 'href="/home/main.html#countriesSection"' 
# just in case it's a relative link in main.html that breaks elsewhere.
new_nav = new_nav.replace('href="/#', 'href="/home/main.html#')

# 3. Process all country pages in pages/
pages_dir = r"C:\Users\recla\zipcode-global\pages"
updated_count = 0
for file in os.listdir(pages_dir):
    if not file.endswith('.html'): continue
    # Skip template and layout
    if file in ('country-template.html', 'layout.html', 'about.html', 'privacy.html', 'report.html', 'translate.html', 'blog.html'):
        continue
    
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace nav block
    html = re.sub(r'<nav class="nav"[^>]*>.*?</nav>', new_nav, html, flags=re.DOTALL)
    
    # Replace script block (from THEMES down to end)
    s_idx = html.find(script_marker)
    e_idx = html.find(end_marker)
    if s_idx != -1 and e_idx != -1:
        # We replace the old chunk with the new one
        html = html[:s_idx] + new_script + html[e_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    updated_count += 1

print(f"Updated {updated_count} country pages with new script & nav.")

# 4. Process all blog posts
blog_dir = r"C:\Users\recla\zipcode-global\pages\blog"
blog_count = 0
for file in os.listdir(blog_dir):
    if not file.endswith('.html'): continue
    filepath = os.path.join(blog_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    html = re.sub(r'<nav class="nav"[^>]*>.*?</nav>', new_nav, html, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    blog_count += 1

print(f"Updated {blog_count} blog posts with new nav.")
