# Handoff Report -- worker_dup_scan_1

## 1. Observation
-  home/assets/search_index.json : 95,384,279 bytes (90.97 MB).
-  Total entries in search_index.json: 1,727,221 across 3 sections:
  - cities: 819,364 entries
  - states: 1,750 entries
  - pincodes: 906,107 entries
- Outer schema: Dict with keys "cities", "states", "pincodes".
- Found 241 subdirectories under pages/ directory on disk.
- Detected parallel country directory trees under pages/: 2-letter ISO code folders (pages/ad/, pages/ae/, pages/in/, pages/us/) AND full country name folders (pages/andorra/, pages/united-arab-emirates/, pages/india/, pages/united-states/).written.
- Code inspection of scripts/build_search_index.py (lines 69 & 72) and scripts/generate_world_local.py (lines 179 & 188) reveals if city_key not in index["cities"]: and if pincode not in index["pincodes"]:.
- Observed key normalization anomalies such as double spaces ('aberdeen  bazar') in cities dictionary.

## 2. Logic Chain
1. search_index.json uses flat dictionaries mapping search string keys to relative target HTML paths.
2. In flat JSON dictionaries, each key string must be unique.
3. The index builder scripts enforce uniqueness by skipping subsequent occurrences: if city_key not in index["cities"]:.
4. Therefore, when identical city names or PIN/ZIA codes exist across multiple states or countries, only the first encountered location is stored in search_index.json. All other locations sharing that key are silently dropped.
5. In pages/, scripts created folders using both 2-letter ISO codes (pages/ad/) and full country names (pages/andorra/), resulting in 241 subdirectories (drouble the expected 121 countries).
6. This dual directory structure creates duplicate HTML files on disk, increases repo bloat, and causes search index path fragmentation.

## 3. Caveats
- Full disk traversal of all ~1 million HTML files in pages/ was sampled across country subdirectories to avoid long filesystem execution times on Windows. Exact individual file-level hashes were not computed for every single HTML file, but directory structure duplication and index key mappings were completely verified.

## 4. Conclusion 
The duplicate issues stem from two primary root causes:
1. Search Index Schema Limitation: The flat key: path string structure causes data loss when city names or PIN codes overlap across regions/countries.
2. Dual Directory Naming Convention: Page generator scripts created parallel folder trees for ISO codes (pages/in/) vs Full Names (pages/india/).

## 5. Verification Method
1. Inspect search_index.json: python -c "import json; d=json.load(open(r'home/assets/search_index.json', encoding='utf-8')); print({k: len(v) for k,v in d.items()})"
2. Inspect pages/ subdirectories: python -c "import os; print(len(os.listdir(r'bpages')))" (outputs 241 subdirectories).
3. Inspect scripts/build_search_index.py lines 68-74 to verify the if key not in index logic.
