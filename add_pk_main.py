import os

main_file = r'C:\Users\recla\zipcode-global\home\main.html'
with open(main_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add Pakistan to COUNTRIES array in main.html
pk_data = "{code:'PK',name:'Pakistan',region:'asia',term:'Postal Code',phone:'+92', lat:30.3753,lon:69.3451},"
if "code:'PK'" not in content:
    # Insert it right before PL
    content = content.replace("{code:'PL',name:'Poland'", pk_data + "\n    {code:'PL',name:'Poland'")
    with open(main_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Pakistan to main.html COUNTRIES list.")
else:
    print("Pakistan is already in the main.html COUNTRIES list.")
