import os
import json
import time
from collections import defaultdict

base_dir = os.path.abspath(r'C:\Users\recla\zipcode-global')
index_path = os.path.join(base_dir, 'home', 'assets', 'search_index.json')
pages_dir = os.path.join(base_dir, 'pages')

print('--- Step 1: Loading search_index.json ---')
t0 = time.time()
with open(index_path, 'r', encoding='utf-8') as fh:
    index = json.load(fh)
t1 = time.time()
print('Loaded search_index.json in', round(t1-t0, 2), 's')

cities = index.get('cities', {})
states = index.get('states', {})
pincodes = index.get('pincodes', {})

print('Cities count:', len(cities))
print('States count:', len(states))
print('Pincodes count:', len(pincodes))
total_keys = len(cities) + len(states) + len(pincodes)
print('Total keys in index:', total_keys)

# 1. Normalization & Key Anomalies
print('\n=== Key Normalization Analysis ===')
for sec_name, sec_dict in [('cities', cities), ('states', states), ('pincodes', pincodes)]:
    upper = [k for k in sec_dict if k != k.lower()]
    space = [k for k in sec_dict if k != k.strip()]
    dspace = [k for k in sec_dict if '  ' in k]
    non_ascii = [k for k in sec_dict if not k.isascii()]
    print(sec_name, '- Upper:', len(upper), 'Leading/Trailing Space:', len(space), 'DoubleSpace:', len(dspace), 'NonASCII:', len(non_ascii))

# 2. Path format and collisions
print('\n=== Target URL Collisions (Multiple Keys -> Same Path) ===')
all_index_paths = set()
for sec_name, sec_dict in [('cities', cities), ('states', states), ('pincodes', pincodes)]:
    url_to_keys = defaultdict(list)
    for k, v in sec_dict.items():
        url_to_keys[v].append(k)
        all_index_paths.add(v.lstrip('/'))
    dup_urls = {u: ks for u, ks in url_to_keys.items() if len(ks) > 1}
    print(sec_name, 'Paths mapped to multiple keys:', len(dup_urls))
    if dup_urls:
        sample_u = list(dup_urls.keys())[0]
        print('  Sample collision path:', sample_u, 'Mapped keys count:', len(dup_urls[sample_u]), 'Sample keys:', dup_urls[sample_u][:5])

# 3. Disk Scan of pages/
print('\n=== Disk Scan of pages/ Directory ===')
t2 = time.time()
disk_files = set()
country_counts = defaultdict(int)
casing_map = defaultdict(list)
zero_byte_files = []

for root, dirs, files in os.walk(pages_dir):
    for f in files:
        if f.endswith('.html'):
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, base_dir).replace(chr(92), '/')
            disk_files.add(rel_p)
            parts = rel_p.split('/')
            if len(parts) > 1:
                country_counts[parts[1]] += 1
            casing_map[rel_p.lower()].append(rel_p)
            if os.path.getsize(full_p) == 0:
                zero_byte_files.append(rel_p)

t3 = time.time()
print('Disk scan complete in', round(t3-t2, 2), 's')
print('Total HTML files on disk:', len(disk_files))
print('Country folder file counts:', dict(country_counts))
print('Zero byte HTML files:', len(zero_byte_files))
casing_conflicts = {k: v for k, v in casing_map.items() if len(v) > 1}
print('Casing conflicts on disk:', len(casing_conflicts))
if casing_conflicts:
    print('  Sample casing conflict:', list(casing_conflicts.values())[0])

# 4. Cross-Validation: search_index vs Disk
print('\n=== Cross-Validation: search_index vs Disk ===')
broken_links = all_index_paths - disk_files
orphaned_files = disk_files - all_index_paths
print('Broken links (Indexed paths missing on disk):', len(broken_links))
print('Orphaned files (Disk HTML pages missing in index):', len(orphaned_files))
if broken_links:
    print('  Sample broken link:', list(broken_links)[:5])
if orphaned_files:
    print('  Sample orphaned file:', list(orphaned_files)[:5])
