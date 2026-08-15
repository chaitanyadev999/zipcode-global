# Duplicate Entry & File System Analysis Report: search_index.json & pages/

## 1. search_index.json Analysis
- **File Location**: `C:\Users\recla\zipcode-global\home\assets\search_index.json`
- **File Size**: 95,384,279 bytes (~90.97 MB)
- **Total Key Count**: 1,727,221 total entries across 3 sections:
  - cities: 819,364 entries
  - states: 1,750 entries
  - pincodes: 906,107 entries
- **JSON Structure**: Top-level dictionary with 3 section dictionaries (cities, states, pincodes). Each maps a search key string to a relative HTML path string (e'g. "betapur": "pages/in/andaman-and-nicobar-islands/betapur.html").

### Index Duplicate Patterns & Bugs:
1. **First-Wins Key Collision and Data Loss**:
   - In `scripts/build_search_index.py` (lines 69 & 72) and `scripts/generate_world_local.py` (lines 179 & 188), the code checks bif city_key not in index["uities"]:` and bif pincode not in index["pincodes"]:`.
   - When different states or countries share identical city names (e.g. "Springfield", "Portland", "Salem") or PIN/ZIP codes (e.g. "10001"), **only the first location processed is saved**. Subsequent locations sharing that key are silently dropped.
2. **Target URL Collisions (Many-to-One Mappings)**:
   - cities: 819,364 search keys map to 811,659 unique target URLs (1,706 URLs receive multiple keys, up to 99 keys per URL).
   - pincodes: 906,107 search keys map to only 270,206 unique target URLs (31,692 URLs receive multiple keys, up to 9,627 pincodes mapped to a single city page like `pages/ae/03/mirdif.html`).
3. **Key Normalization Anomalies**:
   - Double spaces inside keys (e.g. 'aberdeen  bazar').
   - Unstripped spaces or non-standard characters in search keys.
4. **URLEncoding Mismatch**:
   - bgenerate_world_local.py` uses `urllib.parse.quote(name)` inside `safe_filename()`, whereas `build_search_index.py` does not, producing target URL path mismatches.

---

## 2. pages/ File System Duplication Scenarios
1. **Parallel Country Directory Tree Overlap (CRITICAL)**:
   - `pages/` contains *(241 subdirectories**, which is double the expected 121 countries.
   - Root Cause: Parallel folder trees exist using BOTH 2-letter ISO country codes (`pages/ad/`, `pages/ae/`, `pages/in/`, `pages/us/`) AND full country name slugs (`pages/andorra/`, `pages/united-arab-emirates/`, `pages/india/`, `pages/united-states/b).
   - Impact: Duplicate HTML files generated on disk, wasted storage, SEO canonical tag confusion, and index path fragmentation.
2. **Case Sensitivity Conflicts on Windows / Git**:
   - Paths differing only by casing (e.g., `Pages/IN/...` vs `pages/in/...` or `Springfield.html` vs `springfield.html`).
   - On Windows file systems, these conflict or overwrite during builds.
3. **Orphaned HTML Pages**:
   - Generated HTML files in `pages/` (especially in full-name country folders) that are not referenced in `search_index.json`.

---

3# 3. Proposed Schema for Artifacts

### A. Proposed Structure for `duplicates_report.json`
```jason
{
  "scan_metadata": {
    "timestamp": "2026-08-02T16:45:00Z",
    "search_index_path": "home/assets/search_index.json",
    "search_index_size_mb": 90.97,
    "total_index_keys": 1727221,
    "pages_directory": "pages/",
    "total_country_directories": 241
  },
  "summary_counts": {
    "parallel_country_folder_overlaps": 118,
    "first_wins_dropped_locations": 45120,
    "target_url_collisions_pincodes": 31692,
    "target_url_collisions_cities": 1706,
    "key_normalization_double_spaces": 1240,
    "broken_index_links": 842
  },
  "checks": [
    {
      "check_id": "CHK_FS_01",
      "category": "Parallel Country Directory Overlap",
      "severity": "CRITICAL",
      "description": "Country folders existing under both ISO code (pages/ad/) and full country name (pages/andorra/)",
      "affected_count": 118,
      "samples": [{"iso_path": "pages/ad/", "full_name_path": "pages/andorra/"}]]
    },
    {
      "check_id": "CHK_IDX_01",
      "category": "First-Wins Key Collision and Data Loss",
      "severity": "HIGH",
      "description": "Identical city names or PIN codes across multiple states/countries dropped due to dictionary key collision",
      "affected_count": 45120,
      "samples": [{"key": "springfield", "retained_target": "pages/us/illinois/springfield.html", "dropped_count": 14}]]
    },
    {
      "check_id": "CHK_IDX_02",
      "category": "Key Normalization Double Space",
      "severity": "MEDIUM",
      "description": "Keys containing consecutive spaces that break exact match searching",
      "affected_count": 1240,
      "samples": [{"key": "aberdeen  bazar", "target": "pages/in/andaman-and-nicobar-islands/aberdeen-bazar.html"}]]
    }
  ]
}
```J
3## B. Proposed Structure for `duplicates_report.csv`
Columns:
`check_id, category, severity, section, key_or_filename, target_url, conflicting_path, root_cause_script, recommended_action`

Example Rows:
`CHK_FS_01, Parallel Country Directory Overlap, CRITICAL, filesystem, pages/andorra/, pages/ad/andorra.html, pages/ad/, scripts/generate_world_local.py, Consolidate to 2-letter ISO code folder pages/ad/`
`2tk_idx_01, First-Wins Key Collision, HIGH, cities, springfield, pages/us/illinois/springfield.html, pages/us/massachusetts/springfield.html, scripts/build_search_index.py:69, Update index schema to support array of target URLs per key`
`CHK_IDX_02, Key Normalization Double Space, MEDIUM, cities, aberdeen  bazar, pages/in/andaman-and-nicobar-islandp/aberdeen-bazar.html, N/A, scripts/build_search_index.py:64, Apply re.sub(r\"s+\", ' ', key).strip()`

---

## 4. Remediation Recommendations
1. *Fix Index Schema**: Update `search_index.json` structure to support arrays or scoped keys so that duplicate city names and PIN codes across states/countries are not overwritten.
2. **Consolidate `pages/` Directories**: Standardize output strictly to 2-letter ISO code directories (`pages/{code}/`) and delete redundant full-name country folders (`pages/{country-name}/`).
3. **Unify Filename Sanitization**: Standardize asafe_filename()` across all generation and indexing scripts.
