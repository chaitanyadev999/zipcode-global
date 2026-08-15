import os

filepath = r"C:\Users\recla\zipcode-global\pages\translate.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove google_translate_element div
html = html.replace('<div id="google_translate_element"></div>', '')

# Remove scripts
s1 = """<script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
}
</script>"""
s2 = """<script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit" async defer></script>"""

html = html.replace(s1, '')
html = html.replace(s2, '')

# Wait, there's another script in head perhaps? 
# Let's clean it up.
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed Google Translate widget from translate.html")
