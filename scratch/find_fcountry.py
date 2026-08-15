import os
with open(r'C:\Users\recla\zipcode-global\home\main.html', encoding='utf-8') as f:
    for i, l in enumerate(f):
        if 'id="fCountry"' in l:
            print("Found fCountry at", i)
            # print the next 20 lines
            for j in range(20):
                print(next(f).strip())
            break
