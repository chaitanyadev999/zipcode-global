import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove duplicate paragraph
dup_text = '<p>Search instant PIN codes, ZIP codes and Postcodes worldwide. Includes complete states, cities, districts, interactive maps & full location details.</p>'
content = content.replace(dup_text + '\n', '')
content = content.replace(dup_text, '')

# 2. Change <article to <div in the FAQ section
content = content.replace('<article style="margin-bottom: 2.5rem;', '<div style="margin-bottom: 2.5rem;')
content = content.replace('</article>', '</div>')

# 3. Add <main id="main"> after </nav> and </main> before <footer>
# Check if <main> is already there
if '<main' not in content:
    content = content.replace('</nav>', '</nav>\n<main id="main">')
    content = content.replace('<footer>', '</main>\n<footer>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed duplicate text, replaced article tags, and added main tags.')
