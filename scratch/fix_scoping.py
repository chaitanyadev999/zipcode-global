import re

path = r'C:\Users\recla\zipcode-global\home\main.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove renderPopular definition and calls
html = re.sub(r'function renderPopular\(\)\{.*?\n\}\n', '', html, flags=re.DOTALL)
html = html.replace('renderPopular();', '')

# 2. Expose Finder functions to window so onchange handlers can find them
exposure_code = """
window.loadFinderStates = loadFinderStates;
window.loadFinderCities = loadFinderCities;
window.gotoFinderCity = gotoFinderCity;
"""

if "window.loadFinderStates =" not in html:
    html = html.replace('function loadFinderStates', exposure_code + '\nasync function loadFinderStates')
    # wait, loadFinderStates is now async function loadFinderStates()
    html = html.replace(exposure_code + '\nasync function loadFinderStates', exposure_code + '\nasync function loadFinderStates')
    
    # Better way to replace:
    if "async function loadFinderStates" in html and "window.loadFinderStates" not in html:
        html = html.replace('async function loadFinderStates', exposure_code + 'async function loadFinderStates')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
