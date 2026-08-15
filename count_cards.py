import os

filepath = 'C:/Users/recla/zipcode-global/pages/blog.html'
txt = open(filepath, 'r', encoding='utf-8').read()

cards = txt.count('class="card"')
imgs = txt.count('<img src')

print(f"{cards} cards, {imgs} images")
