import os

pages_dir = r'C:\Users\recla\zipcode-global\pages'
html_files = [f for f in os.listdir(pages_dir) if f.endswith('.html') and not f.startswith('shared')]

# Read one file to make sure it matches
for f in html_files:
    path = os.path.join(pages_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    orig = content
    
    # 1. Fix City/Division detection order
    content = content.replace(
        'city:  find(/division.?name/,/region.?name/,/^city$/,/^village$/,/^town$/,/place.?name/,/office.?name/,/^locality$/),',
        'city:  find(/^city$/,/^village$/,/^town$/,/place.?name/,/office.?name/,/^locality$/,/division.?name/,/region.?name/),'
    )
    
    # 2. Fix All Countries button -> Home Page
    content = content.replace(
        '<a class="nav-btn primary" href="/home/main.html#countriesSection">🌍 All Countries</a>',
        '<a class="nav-btn primary" href="/home/main.html">🏠 Home Page</a>'
    )
    content = content.replace(
        '<a class="nav-btn" href="/home/main.html">&#8592; All Countries</a>',
        '<a class="nav-btn" href="/home/main.html">🏠 Home Page</a>'
    )
    
    # 3. Dynamic District/County labeling
    # Add subTerm to NAV
    content = content.replace(
        'step:0, stateFile:null, data:[], fields:{}, city:null, district:null,',
        'step:0, stateFile:null, data:[], fields:{}, city:null, district:null, subTerm:\'District\','
    )
    
    # Set subTerm after detectFields
    detect_block = 'NAV.fields = detectFields(NAV.data);'
    detect_rep = '''NAV.fields = detectFields(NAV.data);
    const df = (NAV.fields.dist||'').toLowerCase();
    NAV.subTerm = df.includes('county') ? 'County' : (df.includes('dist') ? 'District' : (df.includes('muni') ? 'Municipality' : 'Region'));
    try{ document.getElementById('s2title').textContent = NAV.subTerm + 's'; }catch(e){}
    try{ document.querySelector('.back-btn[onclick="goBack(2)"]').innerHTML = '&#8592; Back to ' + NAV.subTerm + 's'; }catch(e){}
    '''
    if 'NAV.subTerm = df.includes' not in content:
        content = content.replace(detect_block, detect_rep)
    
    # Replace hardcoded 'District' in rendering
    content = content.replace(
        '$(\'s1title\').textContent = stLabel + \' — Districts\';',
        '$(\'s1title\').textContent = stLabel + \' — \' + NAV.subTerm + \'s\';'
    )
    content = content.replace(
        'setCount(\'s1cnt\', NAV.distsList.length, \'District\');',
        'setCount(\'s1cnt\', NAV.distsList.length, NAV.subTerm);'
    )
    content = content.replace(
        '$(\'search\').placeholder = \'Search PIN Code, city, district...\';',
        '$(\'search\').placeholder = \'Search PIN Code, city, \' + NAV.subTerm.toLowerCase() + \'...\';'
    )
    
    # In search filter logic, make label dynamic if needed
    content = content.replace(
        'if(low === \'county\') label = \'District\';',
        '// if(low === \'county\') label = \'District\';'
    )
    
    if orig != content:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

# Also fix layout.html separately if it has it
layout_path = os.path.join(pages_dir, 'layout.html')
if os.path.exists(layout_path):
    with open(layout_path, 'r', encoding='utf-8') as file:
        l_content = file.read()
    orig_l = l_content
    l_content = l_content.replace(
        '<a class="nav-btn" href="/home/main.html">&#8592; All Countries</a>',
        '<a class="nav-btn" href="/home/main.html">🏠 Home Page</a>'
    )
    if orig_l != l_content:
        with open(layout_path, 'w', encoding='utf-8') as file:
            file.write(l_content)

print(f'Processed {len(html_files)} HTML files.')
