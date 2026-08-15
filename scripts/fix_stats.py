import os

def replace_in_file(filepath, old, new):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(old, new)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix 3: Stats Bar Instability for IN and US
in_path = r"C:\Users\recla\zipcode-global\pages\india.html"
us_path = r"C:\Users\recla\zipcode-global\pages\usa.html"

# Fix statRegions for India
replace_in_file(in_path, 'id="statRegions">—<', 'id="statRegions">37<')

# Fix statRegions for USA (Task 3) and clarify label (Task 7)
replace_in_file(us_path, 'id="statRegions">—<', 'id="statRegions">53<')
replace_in_file(us_path, "subtitle:'Americas · 50 States · ZIP Codes'", "subtitle:'Americas · 50 States & 3 Territories · ZIP Codes'")

print("Fixed stats for IN and US")
