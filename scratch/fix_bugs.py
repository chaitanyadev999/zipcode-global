import re

# --- 1. Fix main.html ---
path = r'C:\Users\recla\zipcode-global\home\main.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix cardNav
html = html.replace("document.getElementById('globeMount').scrollIntoView({behavior:'smooth',block:'center'});", "")

# Remove Labels Section
# We'll use regex to remove from <div class="labels-section"> up to <!-- FEATURED TOP COUNTRIES -->
html = re.sub(r'<div class="labels-section">.*?<!-- FEATURED TOP COUNTRIES -->', '<!-- FEATURED TOP COUNTRIES -->', html, flags=re.DOTALL)

# Fix loadFinderStates
old_states_logic = """  const cPath = 'pages/' + c + '/';
  let statesFound = [];"""

new_states_logic = """  let cName = document.getElementById('fCountry').options[document.getElementById('fCountry').selectedIndex].text;
  let cSlug = cName.toLowerCase().replace(/ /g, '-').replace(/'/g, '');
  if (c === 'in') cSlug = 'india';
  if (c === 'us') cSlug = 'usa';
  const cPath = 'pages/' + cSlug + '/';
  let statesFound = [];"""

html = html.replace(old_states_logic, new_states_logic)

# Fix loadFinderCities
old_cities_logic = """  const sPath = 'pages/' + c + '/' + st + '/';
  let citiesFound = [];"""

new_cities_logic = """  let cName = document.getElementById('fCountry').options[document.getElementById('fCountry').selectedIndex].text;
  let cSlug = cName.toLowerCase().replace(/ /g, '-').replace(/'/g, '');
  if (c === 'in') cSlug = 'india';
  if (c === 'us') cSlug = 'usa';
  const sPath = 'pages/' + cSlug + '/' + st + '/';
  let citiesFound = [];"""

html = html.replace(old_cities_logic, new_cities_logic)

# Fix gotoFinderCity
old_goto_logic = """  if(cy) {
    window.location.href = '../' + cy;
  } else if(st) {
    window.location.href = '../pages/' + c + '/' + st + '.html';
  } else if(c) {
    window.location.href = '../pages/' + c + '.html';
  } else {"""

new_goto_logic = """  let cName = document.getElementById('fCountry').options[document.getElementById('fCountry').selectedIndex].text;
  let cSlug = cName.toLowerCase().replace(/ /g, '-').replace(/'/g, '');
  if (c === 'in') cSlug = 'india';
  if (c === 'us') cSlug = 'usa';
  
  if(cy) {
    window.location.href = '../' + cy;
  } else if(st) {
    window.location.href = '../pages/' + cSlug + '/' + st + '.html';
  } else if(c) {
    window.location.href = '../pages/' + c + '.html';
  } else {"""

html = html.replace(old_goto_logic, new_goto_logic)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)


# --- 2. Fix blog.html ---
blog_path = r'C:\Users\recla\zipcode-global\pages\blog.html'
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_html = f.read()

count = 1
def replace_img(match):
    global count
    res = f'<img src="https://picsum.photos/600/400?random={count}"'
    count += 1
    return res

blog_html = re.sub(r'<img src="/home/assets/blog/cover\d\.png"', replace_img, blog_html)

with open(blog_path, 'w', encoding='utf-8') as f:
    f.write(blog_html)
