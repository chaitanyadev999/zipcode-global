import os
import json

base_path = r'C:\Users\recla\zipcode-global\data\world\IN'

for filename in os.listdir(base_path):
    if not filename.endswith('.json') or filename == 'data.json':
        continue
        
    filepath = os.path.join(base_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    cleaned_data = []
    seen = set()
    
    for row in data:
        # Standardize District and City to Title Case
        if 'district' in row and isinstance(row['district'], str):
            row['district'] = row['district'].strip().title()
        if 'City' in row and isinstance(row['City'], str):
            row['City'] = row['City'].strip().title()
            
        # Filter NA
        if row.get('district') == 'Na' or row.get('district') == 'NA':
            continue
        if row.get('City') == 'Na' or row.get('City') == 'NA':
            continue
            
        # Deduplicate exactly identical rows (same pincode, same district, same city)
        sig = (row.get('pincode'), row.get('district'), row.get('City'))
        if sig not in seen:
            seen.add(sig)
            cleaned_data.append(row)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, separators=(',', ':'))

print("India data cleaned successfully!")
