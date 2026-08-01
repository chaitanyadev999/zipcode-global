import sys
import os

sys.path.append(os.getcwd())
from generate_pages import COUNTRIES

try:
    from countryinfo import CountryInfo
except ImportError:
    pass

lang_map = {}

for row in COUNTRIES:
    cc = row[0]
    c_name = row[1]
    
    # Try countryinfo
    langs = []
    try:
        country = CountryInfo(c_name)
        langs = country.languages()
    except Exception as e:
        pass
        
    # Manual overrides for accuracy and to use google translate supported codes
    if cc == "IN": langs = ["hi", "te", "ta", "mr", "gu", "kn", "ml", "pa", "bn", "ur", "as", "or"]
    elif cc == "US": langs = ["es", "zh-CN", "tl", "vi", "ar", "fr", "ko", "ru", "de"]
    elif cc == "BR": langs = ["pt"]
    elif cc == "CA": langs = ["en", "fr", "zh-CN", "pa"]
    elif cc == "GB": langs = ["en", "cy", "gd", "ga"]
    elif cc == "CN": langs = ["zh-CN", "zh-TW"]
    elif cc == "KR": langs = ["ko"]
    elif cc == "JP": langs = ["ja"]
    elif cc == "MX": langs = ["es"]
    elif cc == "DE": langs = ["de"]
    elif cc == "FR": langs = ["fr"]
    elif cc == "IT": langs = ["it"]
    elif cc == "ES": langs = ["es", "ca", "gl", "eu"]
    elif cc == "RU": langs = ["ru", "tt"]
    elif cc == "ZA": langs = ["af", "zu", "xh", "st"]
    elif cc == "NG": langs = ["ha", "ig", "yo"]
    elif cc == "BD": langs = ["bn"]
    elif cc == "PK": langs = ["ur", "pa", "sd", "ps"]
    
    # Ensure English is always an option so they can turn it off/on easily (it"s default but good to have)
    final_langs = ["en"]
    if isinstance(langs, list):
        for l in langs:
            # Map standard iso-639-1 to google translate if needed, but mostly they match
            if len(l) == 2 or len(l) == 5:
                if l not in final_langs: final_langs.append(l)
    elif isinstance(langs, dict):
        pass # Handle if needed
        
    lang_map[cc] = ",".join(final_langs)

print("Generated mapping for", len(lang_map), "countries.")

# Let"s just modify generate_pages.py to insert this mapping logic
import re

with open("generate_pages.py", "r", encoding="utf-8") as f:
    content = f.read()
    
# We will create a dictionary string in Python
dict_str = "COUNTRY_LANGS = {\n"
for k, v in lang_map.items():
    dict_str += f"    \"{k.lower()}\": \"{v}\",\n"
dict_str += "}\n"

if "COUNTRY_LANGS =" not in content:
    # insert after COUNTRIES = [...]
    content = re.sub(r"(COUNTRIES = \[.*?\]\n)", r"\1\n" + dict_str, content, flags=re.DOTALL)
    
# Now modify the script tag replacement in generate_pages
new_script = """<script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en', includedLanguages: '{{INCLUDED_LANGS}}', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
}
</script>"""

content = re.sub(
    r"<script type=\"text/javascript\">\nfunction googleTranslateElementInit\(\) \{\n  new google\.translate\.TranslateElement\(\{pageLanguage: 'en', layout: google\.translate\.TranslateElement\.InlineLayout\.SIMPLE\}, 'google_translate_element'\);\n\}\n</script>",
    new_script,
    content
)

# Replace the {{INCLUDED_LANGS}} during file generation
loop_find = "    # Read the country template\n    html = template"
loop_replace = """    # Get language string
    langs = COUNTRY_LANGS.get(code, "en,es,fr,de,zh-CN,ar,hi,pt,ru,ja")
    
    # Read the country template
    html = template.replace("{{INCLUDED_LANGS}}", langs)"""

if "COUNTRY_LANGS.get(code" not in content:
    content = content.replace("    # Read the country template\n    html = template", loop_replace)

with open("generate_pages.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated generate_pages.py successfully!")
