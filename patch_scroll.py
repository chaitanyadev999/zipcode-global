import re

with open('pages/shared_pseo.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace all scrollIntoView with if(shouldScroll) { ... }
js = re.sub(
    r"setTimeout\(\(\) => \$\('resultsSection'\)\.scrollIntoView\(\{ behavior: 'smooth', block: 'start' \}\), 100\);",
    r"if(shouldScroll) { setTimeout(() => $('resultsSection').scrollIntoView({ behavior: 'smooth', block: 'start' }), 100); }",
    js
)

# And make sure local search button/enter sets shouldScroll=true
js = js.replace(
    "$('#searchBtn').addEventListener('click', () => performLocalSearch($('#searchInput').value.trim()));",
    "$('#searchBtn').addEventListener('click', () => performLocalSearch($('#searchInput').value.trim(), true));"
)
js = js.replace(
    "$('#searchInput').addEventListener('keypress', (e) => { if (e.key === 'Enter') $('#searchBtn').click(); });",
    "$('#searchInput').addEventListener('keypress', (e) => { if (e.key === 'Enter') performLocalSearch($('#searchInput').value.trim(), true); });"
)
js = js.replace(
    "function performLocalSearch(query) {",
    "function performLocalSearch(query, shouldScroll=false) {"
)

with open('pages/shared_pseo.js', 'w', encoding='utf-8') as f:
    f.write(js)
    
print("Regex replace applied")
