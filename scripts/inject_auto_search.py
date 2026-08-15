import os
import glob

# Script to inject the auto-search logic before </body> on all country pages
auto_search_js = """
<!-- Auto-Search Logic -->
<script>
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    try {
      const q = new URLSearchParams(window.location.search).get('q');
      if(q && document.getElementById('search')) {
        document.getElementById('search').value = q;
        if(typeof window.doSearch === 'function') {
           window.doSearch();
        } else {
           console.log("doSearch not found, waiting...");
           // try again in 1s
           setTimeout(() => { if(typeof window.doSearch === 'function') window.doSearch(); }, 1000);
        }
      }
    } catch(e) {}
  }, 500);
});
</script>
</body>
"""

pages_dir = r"C:\Users\recla\zipcode-global\pages"
country_html_files = [f for f in os.listdir(pages_dir) if f.endswith('.html') and f not in ('about.html', 'blog.html', 'translate.html', 'privacy.html', 'terms.html')]

for f in country_html_files:
    path = os.path.join(pages_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if "<!-- Auto-Search Logic -->" not in content:
        content = content.replace("</body>", auto_search_js)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Injected into {f}")
    else:
        print(f"Already injected in {f}")

print("Done injecting auto-search JS.")
