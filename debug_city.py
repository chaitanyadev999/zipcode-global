import glob, re
try:
    files = glob.glob('pages/*/*/*.html') + glob.glob('pages/*/*.html')
    files = [f for f in files if '\\pages\\' not in f]
    
    f = files[0]
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
        
    print(f)
    city_match = re.search(r'window\.PSEO_CITY="([^"]+)";', text)
    state_match = re.search(r'window\.PSEO_STATE_LABEL="([^"]+)";', text)
    if not state_match:
        state_match = re.search(r'window\.PSEO_STATE="([^"]+)";', text)
        
    country_match = re.search(r'window\.PSEO_COUNTRY="([^"]+)";', text)

    print('City:', city_match)
    print('State:', state_match)
    print('Country:', country_match)

    if city_match and state_match and country_match:
        start_idx = text.find('<div class="seo-text">')
        end_idx = text.find('</div>', start_idx)
        print('Start:', start_idx, 'End:', end_idx)
    else:
        print("Missing variables!")
except Exception as e:
    print(e)
