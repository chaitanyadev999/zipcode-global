import os

filepaths = os.listdir('C:/Users/recla/zipcode-global/pages/blog')
for f in filepaths:
    if f.endswith('.html'):
        path = 'C:/Users/recla/zipcode-global/pages/blog/' + f
        txt = open(path, 'r', encoding='utf-8').read()
        if 'class="cover"' not in txt:
            print(f"No cover image in {f}")
