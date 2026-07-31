import re

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Hero label
content = content.replace('<span class="hs-l">Regions</span>', '<span class="hs-l" id="statRegionsLabel">Regions</span>')

# Replace s0 title
content = content.replace('<h2 class="sec-title" id="s0title">Choose a Region</h2>', '<h2 class="sec-title" id="s0title">Choose a Region</h2>')

# Replace loadStates logic
old_load = """      $('statRegions').textContent = states.length;
      setCount('s0cnt', states.length, 'Region');"""

new_load = """      $('statRegions').textContent = states.length;
      const sLabel = C.code === 'IN' ? 'State' : 'Region';
      $('s0title').textContent = 'Choose a ' + sLabel;
      $('statRegionsLabel').textContent = sLabel + 's';
      setCount('s0cnt', states.length, sLabel);"""

content = content.replace(old_load, new_load)

# Replace back button text in s1
old_back1 = """<button class="back-btn" onclick="goBack(1)">&#8592; Back to Regions</button>"""
new_back1 = """<button class="back-btn" id="s1back" onclick="goBack(1)">&#8592; Back to Regions</button>"""
content = content.replace(old_back1, new_back1)

old_init = """    // Set page title and meta dynamically"""
new_init = """    if(C.code === 'IN') {
      const s1back = document.getElementById('s1back');
      if(s1back) s1back.innerHTML = '&#8592; Back to States';
    }
    // Set page title and meta dynamically"""
content = content.replace(old_init, new_init)

with open(r'C:\Users\recla\zipcode-global\generate_pages.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_pages.py updated labels successfully!")
