import os

files = ["C:/Users/recla/zipcode-global/home/main.html", 
         "C:/Users/recla/zipcode-global/pages/about.html", 
         "C:/Users/recla/zipcode-global/pages/privacy.html", 
         "C:/Users/recla/zipcode-global/pages/report.html", 
         "C:/Users/recla/zipcode-global/pages/blog.html"]

langs = "en,es,fr,de,zh-CN,ar,hi,pt,ru,ja,ko,it,nl"
for path in files:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = content.replace(
            "new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');",
            f"new google.translate.TranslateElement({{pageLanguage: 'en', includedLanguages: '{langs}', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}}, 'google_translate_element');"
        )
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Patched {path}")
