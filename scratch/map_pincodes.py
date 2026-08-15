import os
import json
import re

index_path = r'C:\Users\recla\zipcode-global\home\assets\search_index.json'
with open(index_path, 'r', encoding='utf-8') as f:
    idx_data = json.load(f)

def clean_key(s):
    return re.sub(r'[^a-z0-9\s-]', '', str(s).lower()).strip().replace(' ', '-')

data_dirs = [
    r'C:\Users\recla\zipcode-global\scratch\pincode-dataindia',
    r'C:\Users\recla\zipcode-global\data'
]

pincode_count = 0

for d in data_dirs:
    if not os.path.exists(d): continue
    for f in os.listdir(d):
        if f.endswith('.json') and f != 'tree.json' and f != 'duplicates_report.json':
            path = os.path.join(d, f)
            try:
                with open(path, 'r', encoding='utf-8') as jf:
                    records = json.load(jf)
                    for r in records:
                        pin = str(r.get('pincode', r.get('zip', r.get('postal_code', '')))).strip()
                        if not pin: continue
                        
                        city = r.get('officename', r.get('city', r.get('village', r.get('place_name', r.get('divisionname', r.get('districtname', ''))))))
                        if not city: continue
                        
                        c_slug = clean_key(city)
                        if c_slug in idx_data['cities']:
                            idx_data['pincodes'][pin] = idx_data['cities'][c_slug]
                            pincode_count += 1
            except Exception as e:
                pass

if pincode_count > 0:
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(idx_data, f, separators=(',', ':'))

print(f"Mapped {pincode_count} pincodes in search_index.json")
