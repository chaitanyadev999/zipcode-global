import os
import json
import csv
import time
import re
from collections import defaultdict
from datetime import datetime, timezone

# ISO 2-letter country codes to exact full name country slug(s)
ISO_TO_COUNTRY_SLUGS = {
    'ad': ['andorra'],
    'ae': ['united-arab-emirates'],
    'ai': ['anguilla'],
    'al': ['albania'],
    'ar': ['argentina'],
    'as': ['american-samoa'],
    'at': ['austria'],
    'au': ['australia'],
    'ax': ['aland-islands'],
    'az': ['azerbaijan'],
    'bd': ['bangladesh'],
    'be': ['belgium'],
    'bg': ['bulgaria'],
    'bm': ['bermuda'],
    'br': ['brazil'],
    'by': ['belarus'],
    'ca': ['canada'],
    'cc': ['cocos-islands'],
    'ch': ['switzerland'],
    'cl': ['chile'],
    'cn': ['china'],
    'co': ['colombia'],
    'cr': ['costa-rica'],
    'cx': ['christmas-island'],
    'cy': ['cyprus'],
    'cz': ['czech-republic'],
    'de': ['germany'],
    'dk': ['denmark'],
    'do': ['dominican-republic'],
    'dz': ['algeria'],
    'ec': ['ecuador'],
    'ee': ['estonia'],
    'es': ['spain'],
    'fi': ['finland'],
    'fk': ['falkland-islands'],
    'fm': ['micronesia'],
    'fo': ['faroe-islands'],
    'fr': ['france'],
    'gb': ['united-kingdom'],
    'gf': ['french-guiana'],
    'gg': ['guernsey'],
    'gi': ['gibraltar'],
    'gl': ['greenland'],
    'gp': ['guadeloupe'],
    'gs': ['south-georgia'],
    'gt': ['guatemala'],
    'gu': ['guam'],
    'hk': ['hong-kong'],
    'hm': ['heard-island'],
    'hn': ['honduras'],
    'hr': ['croatia'],
    'ht': ['haiti'],
    'hu': ['hungary'],
    'id': ['indonesia'],
    'ie': ['ireland'],
    'im': ['isle-of-man'],
    'in': ['india'],
    'io': ['british-indian-ocean'],
    'is': ['iceland'],
    'it': ['italy'],
    'je': ['jersey'],
    'jp': ['japan'],
    'ke': ['kenya'],
    'kr': ['south-korea'],
    'li': ['liechtenstein'],
    'lk': ['sri-lanka'],
    'lt': ['lithuania'],
    'lu': ['luxembourg'],
    'lv': ['latvia'],
    'ma': ['morocco'],
    'mc': ['monaco'],
    'md': ['moldova'],
    'mh': ['marshall-islands'],
    'mk': ['north-macedonia'],
    'mo': ['macao'],
    'mp': ['northern-mariana-islands'],
    'mq': ['martinique'],
    'mt': ['malta'],
    'mw': ['malawi'],
    'mx': ['mexico'],
    'my': ['malaysia'],
    'nc': ['new-caledonia'],
    'nf': ['norfolk-island'],
    'nl': ['netherlands'],
    'no': ['norway'],
    'nr': ['nauru'],
    'nu': ['niue'],
    'nz': ['new-zealand'],
    'pa': ['panama'],
    'pe': ['peru'],
    'pf': ['french-polynesia'],
    'ph': ['philippines'],
    'pk': ['pakistan'],
    'pl': ['poland'],
    'pm': ['saint-pierre'],
    'pn': ['pitcairn'],
    'pr': ['puerto-rico'],
    'pt': ['portugal'],
    'pw': ['palau'],
    're': ['reunion'],
    'ro': ['romania'],
    'rs': ['serbia'],
    'ru': ['russia'],
    'se': ['sweden'],
    'sg': ['singapore'],
    'si': ['slovenia'],
    'sj': ['svalbard'],
    'sk': ['slovakia'],
    'sm': ['san-marino'],
    'tc': ['turks-and-caicos'],
    'th': ['thailand'],
    'tr': ['turkey'],
    'ua': ['ukraine'],
    'us': ['united-states', 'usa'],
    'uy': ['uruguay'],
    'va': ['vatican-city'],
    'vi': ['us-virgin-islands'],
    'wf': ['wallis-and-futuna'],
    'ws': ['samoa'],
    'yt': ['mayotte'],
    'za': ['south-africa']
}

def main():
    start_time = datetime.now(timezone.utc)
    base_dir = os.path.abspath(r'C:\Users\recla\zipcode-global')
    index_path = os.path.join(base_dir, 'home', 'assets', 'search_index.json')
    pages_dir = os.path.join(base_dir, 'pages')

    print('=== 1. Loading search_index.json ===')
    t0 = time.time()
    with open(index_path, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
    t1 = time.time()
    print(f'Loaded search_index.json in {round(t1-t0, 2)}s')

    cities = index_data.get('cities', {})
    states = index_data.get('states', {})
    pincodes = index_data.get('pincodes', {})
    total_keys = len(cities) + len(states) + len(pincodes)

    all_indexed_paths = set()
    url_to_keys = defaultdict(list)
    key_norm_issues = []
    key_tracker = defaultdict(list)

    # Process all sections: cities, states, pincodes
    for sec_name, sec_dict in [('cities', cities), ('states', states), ('pincodes', pincodes)]:
        for key, target_url in sec_dict.items():
            norm_target = target_url.lstrip('/')
            all_indexed_paths.add(norm_target)
            url_to_keys[(sec_name, norm_target)].append(key)
            key_tracker[key].append({'section': sec_name, 'target_url': target_url})
            if '  ' in key or key != key.strip():
                key_norm_issues.append({'section': sec_name, 'key': key, 'target_url': target_url})

    target_collisions_cities = []
    target_collisions_states = []
    target_collisions_pincodes = []
    for (sec_name, target_url), keys in url_to_keys.items():
        if len(keys) > 1:
            item = {'target_url': target_url, 'keys_count': len(keys), 'sample_keys': keys[:5]}
            if sec_name == 'cities':
                target_collisions_cities.append(item)
            elif sec_name == 'states':
                target_collisions_states.append(item)
            elif sec_name == 'pincodes':
                target_collisions_pincodes.append(item)

    key_cross_section_dups = []
    for key, occurrences in key_tracker.items():
        if len(occurrences) > 1:
            sections_found = list(set([o['section'] for o in occurrences]))
            key_cross_section_dups.append({
                'key': key,
                'occurrences_count': len(occurrences),
                'sections': sections_found,
                'targets': [o['target_url'] for o in occurrences[:5]]
            })

    print('=== 2. Scanning pages/ country directories & checking target links ===')
    t2 = time.time()
    country_subdirs = [d for d in os.listdir(pages_dir) if os.path.isdir(os.path.join(pages_dir, d))]

    # Exact ISO-to-Country Slug mapping check for CHK_FS_01
    parallel_folder_overlaps = []
    for iso, slugs in ISO_TO_COUNTRY_SLUGS.items():
        iso_p = os.path.join(pages_dir, iso)
        if os.path.isdir(iso_p):
            iso_subdirs = set(os.listdir(iso_p))
            for slug in slugs:
                slug_p = os.path.join(pages_dir, slug)
                if os.path.isdir(slug_p):
                    slug_subdirs = set(os.listdir(slug_p))
                    overlap = iso_subdirs.intersection(slug_subdirs)
                    parallel_folder_overlaps.append({
                        'iso_code': iso,
                        'iso_path': f'pages/{iso}/',
                        'full_name': slug,
                        'full_name_path': f'pages/{slug}/',
                        'overlapping_directories_count': len(overlap),
                        'iso_subdirs_count': len(iso_subdirs),
                        'full_name_subdirs_count': len(slug_subdirs)
                    })

    # Comprehensive link existence check across all indexed paths
    broken_links = [p for p in all_indexed_paths if not os.path.exists(os.path.join(base_dir, p))]

    t3 = time.time()
    print(f'Disk scan complete in {round(t3-t2, 2)}s. Found {len(country_subdirs)} country subdirs & {len(broken_links)} broken links.')

    print('=== 3. Writing duplicates_report.json & duplicates_report.csv ===')

    json_report = {
        'scan_metadata': {
            'timestamp': start_time.isoformat(),
            'search_index_path': 'home/assets/search_index.json',
            'search_index_size_mb': round(os.path.getsize(index_path) / (1024 * 1024), 2),
            'total_index_keys': total_keys,
            'cities_count': len(cities),
            'states_count': len(states),
            'pincodes_count': len(pincodes),
            'pages_directory': 'pages/',
            'total_country_directories': len(country_subdirs)
        },
        'summary_counts': {
            'parallel_country_folder_overlaps': len(parallel_folder_overlaps),
            'target_url_collisions_cities': len(target_collisions_cities),
            'target_url_collisions_states': len(target_collisions_states),
            'target_url_collisions_pincodes': len(target_collisions_pincodes),
            'key_normalization_issues': len(key_norm_issues),
            'cross_section_exact_duplicate_keys': len(key_cross_section_dups),
            'broken_index_links_count': len(broken_links)
        },
        'checks': [
            {
                'check_id': 'CHK_FS_01',
                'category': 'Parallel Country Directory Overlap',
                'severity': 'CRITICAL',
                'description': 'Dual country directories existing under both ISO code and full country name slug.',
                'affected_count': len(parallel_folder_overlaps),
                'samples': parallel_folder_overlaps[:20]
            },
            {
                'check_id': 'CHK_IDX_01',
                'category': 'Target URL Collision (Cities)',
                'severity': 'HIGH',
                'description': 'Multiple city search keys mapping to identical target HTML URL.',
                'affected_count': len(target_collisions_cities),
                'samples': target_collisions_cities[:20]
            },
            {
                'check_id': 'CHK_IDX_01_S',
                'category': 'Target URL Collision (States)',
                'severity': 'HIGH',
                'description': 'Multiple state search keys mapping to identical target HTML URL.',
                'affected_count': len(target_collisions_states),
                'samples': target_collisions_states[:20]
            },
            {
                'check_id': 'CHK_IDX_02',
                'category': 'Target URL Collision (Pincodes)',
                'severity': 'HIGH',
                'description': 'Multiple pincode search keys mapping to identical target HTML URL.',
                'affected_count': len(target_collisions_pincodes),
                'samples': target_collisions_pincodes[:20]
            },
            {
                'check_id': 'CHK_IDX_03',
                'category': 'Key Normalization Anomaly',
                'severity': 'MEDIUM',
                'description': 'Keys with consecutive spaces or leading/trailing whitespace across cities, states, and pincodes.',
                'affected_count': len(key_norm_issues),
                'samples': key_norm_issues[:20]
            },
            {
                'check_id': 'CHK_IDX_04',
                'category': 'Broken Index Target Links',
                'severity': 'HIGH',
                'description': 'Relative target HTML paths in search index that do not exist on disk.',
                'affected_count': len(broken_links),
                'samples': broken_links[:20]
            },
            {
                'check_id': 'CHK_IDX_05',
                'category': 'Cross-Section Duplicate Keys',
                'severity': 'MEDIUM',
                'description': 'Search keys appearing across multiple sections (cities, states, pincodes).',
                'affected_count': len(key_cross_section_dups),
                'samples': key_cross_section_dups[:20]
            }
        ]
    }

    report_json_path = os.path.join(base_dir, 'duplicates_report.json')
    with open(report_json_path, 'w', encoding='utf-8') as f:
        json.dump(json_report, f, indent=2)

    csv_rows = []

    # 1. Parallel country directory overlaps (CHK_FS_01)
    for item in parallel_folder_overlaps:
        fn_path = item['full_name_path']
        iso_path = item['iso_path']
        csv_rows.append({
            'check_id': 'CHK_FS_01',
            'category': 'Parallel Country Directory Overlap',
            'severity': 'CRITICAL',
            'section': 'filesystem',
            'key_or_filename': item['full_name'],
            'target_url': fn_path,
            'conflicting_path': iso_path,
            'root_cause_script': 'scripts/generate_world_local.py',
            'recommended_action': f'Consolidate {fn_path} into {iso_path}'
        })

    # 2. Target URL collisions - Cities (CHK_IDX_01)
    for item in target_collisions_cities[:500]:
        csv_rows.append({
            'check_id': 'CHK_IDX_01',
            'category': 'Target URL Collision (Cities)',
            'severity': 'HIGH',
            'section': 'cities',
            'key_or_filename': '|'.join(item['sample_keys']),
            'target_url': item['target_url'],
            'conflicting_path': 'N/A',
            'root_cause_script': 'scripts/build_search_index.py:69',
            'recommended_action': 'Update search_index.json to support key to array of URLs'
        })

    # 3. Target URL collisions - States (CHK_IDX_01_S)
    for item in target_collisions_states[:500]:
        csv_rows.append({
            'check_id': 'CHK_IDX_01_S',
            'category': 'Target URL Collision (States)',
            'severity': 'HIGH',
            'section': 'states',
            'key_or_filename': '|'.join(item['sample_keys']),
            'target_url': item['target_url'],
            'conflicting_path': 'N/A',
            'root_cause_script': 'scripts/build_search_index.py:69',
            'recommended_action': 'Update search_index.json to support key to array of URLs'
        })

    # 4. Target URL collisions - Pincodes (CHK_IDX_02)
    for item in target_collisions_pincodes[:500]:
        csv_rows.append({
            'check_id': 'CHK_IDX_02',
            'category': 'Target URL Collision (Pincodes)',
            'severity': 'HIGH',
            'section': 'pincodes',
            'key_or_filename': '|'.join(item['sample_keys']),
            'target_url': item['target_url'],
            'conflicting_path': 'N/A',
            'root_cause_script': 'scripts/build_search_index.py:72',
            'recommended_action': 'Update search_index.json to support key to array of URLs'
        })

    # 5. Key Normalization Anomalies (CHK_IDX_03)
    for item in key_norm_issues[:500]:
        csv_rows.append({
            'check_id': 'CHK_IDX_03',
            'category': 'Key Normalization Anomaly',
            'severity': 'MEDIUM',
            'section': item['section'],
            'key_or_filename': item['key'],
            'target_url': item['target_url'],
            'conflicting_path': 'N/A',
            'root_cause_script': 'scripts/build_search_index.py:64',
            'recommended_action': 'Normalize key spaces'
        })

    # 6. Broken Index Target Links (CHK_IDX_04)
    for path in broken_links[:500]:
        csv_rows.append({
            'check_id': 'CHK_IDX_04',
            'category': 'Broken Index Target Links',
            'severity': 'HIGH',
            'section': 'index',
            'key_or_filename': os.path.basename(path),
            'target_url': path,
            'conflicting_path': 'N/A',
            'root_cause_script': 'scripts/build_search_index.py',
            'recommended_action': 'Fix or remove broken link from search index'
        })

    fieldnames = ['check_id', 'category', 'severity', 'section', 'key_or_filename', 'target_url', 'conflicting_path', 'root_cause_script', 'recommended_action']
    report_csv_path = os.path.join(base_dir, 'duplicates_report.csv')
    with open(report_csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_rows)

    print('SUCCESS: Created duplicates_report.json and duplicates_report.csv')

if __name__ == '__main__':
    main()
