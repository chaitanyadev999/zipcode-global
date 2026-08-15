import json
import os

index_path = r'C:\Users\recla\zipcode-global\home\assets\search_index.json'

with open(index_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

invalid_pages = ['about', 'blog', 'country-template', 'layout', 'privacy', 'report', 'translate']
removed = 0

for page in invalid_pages:
    if page in data['countries']:
        del data['countries'][page]
        removed += 1

with open(index_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, separators=(',', ':'))

print(f"Removed {removed} invalid pages. Total valid countries: {len(data['countries'])}")
