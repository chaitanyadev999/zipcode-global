import os

files = ["about.html", "privacy.html", "report.html", "blog.html"]
for f in files:
    path = os.path.join("C:/Users/recla/zipcode-global/pages", f)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        
        content = content.replace("src=\"//translate.google.com/translate_a/element.js", "src=\"https://translate.google.com/translate_a/element.js")
            
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Patched {f}")
