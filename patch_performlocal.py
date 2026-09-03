import re

with open('pages/shared_pseo.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix performLocalSearch
js = js.replace("function performLocalSearch(q) {", "function performLocalSearch(q, shouldScroll=false) {")
js = js.replace("$('searchBtn').addEventListener('click', () => performLocalSearch($('searchInput').value.trim()));", "$('searchBtn').addEventListener('click', () => performLocalSearch($('searchInput').value.trim(), true));")
js = js.replace("$('searchInput').addEventListener('keypress', (e) => { if (e.key === 'Enter') $('searchBtn').click(); });", "$('searchInput').addEventListener('keypress', (e) => { if (e.key === 'Enter') performLocalSearch($('searchInput').value.trim(), true); });")

with open('pages/shared_pseo.js', 'w', encoding='utf-8') as f:
    f.write(js)
