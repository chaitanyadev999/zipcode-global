import os
import re

files = ["about.html", "privacy.html", "report.html", "blog.html"]

translate_css = """
  /* Google Translate styling */
  #google_translate_element { display:inline-block; margin-left: 10px; vertical-align: middle; }
  .goog-te-gadget { font-family: var(--f) !important; color: transparent !important; font-size:0; }
  .goog-te-gadget .goog-te-combo { 
    background: var(--glass); border: 1px solid var(--b); color: var(--t2); 
    padding: .4rem .9rem; border-radius: 999px; font-weight: 600; font-size: .8rem;
    cursor: pointer; transition: all .25s var(--ease); outline: none;
  }
  .goog-te-gadget .goog-te-combo:hover { background: var(--card-hi); border-color: var(--cyan); color: var(--t); }
  .goog-te-gadget .goog-te-combo option { background: #050816; color: #fff; font-weight:normal; }
  .skiptranslate iframe { display: none !important; }
  body { top: 0 !important; }
</style>
"""

translate_script = """
<script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: "en", layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, "google_translate_element");
}
</script>
<script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit" async defer></script>
</body>
"""

for f in files:
    path = os.path.join("C:/Users/recla/zipcode-global/pages", f)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Remove translator link
        content = re.sub(r'<a[^>]*href="[^"]*translate\.html"[^>]*>Translator</a>\s*', "", content)
        
        # Insert google translate element into nav-links if not there
        if "google_translate_element" not in content:
            # find the end of nav-links
            content = re.sub(r'(</div>\s*</nav>)', r'  <div id="google_translate_element"></div>\n    \1', content)
            
            # insert CSS before </style>
            content = content.replace("</style>", translate_css)
            
            # insert Script before </body>
            content = content.replace("</body>", translate_script)
            
        # fix z-index in nav
        content = re.sub(r'\.nav\{position:fixed;top:0;left:0;right:0;z-index:\d+;', '.nav{position:fixed;top:0;left:0;right:0;z-index:9999;', content)
            
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Patched {f}")
