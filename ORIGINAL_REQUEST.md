# Original User Request

## 2026-08-02T11:09:43Z

Scan the `search_index.json` and the generated HTML files/folders across the project to identify duplicate entries, redundant files, or overlapping data. Generate a comprehensive JSON or CSV report of all found duplicates.

Working directory: `C:\Users\recla\zipcode-global`
Integrity mode: development

## Requirements

### R1. Search Index Duplicates
Analyze `C:\Users\recla\zipcode-global\home\assets\search_index.json` to find identical or conflicting entries (e.g., same ZIP code in same city pointing to different paths, or duplicate path references).

### R2. File System Duplicates
Scan the generated HTML folders (e.g. `C:\Users\recla\zipcode-global\pages\in\`, `pages\us\`) to find duplicate file names or folders that shouldn't coexist.

### R3. Output Report
Generate a clean, structured report (CSV or JSON format) listing all discovered duplicates, their locations, and the nature of the duplication.

## Acceptance Criteria

### Verification
- [ ] A Python script is created that automatically performs the scanning of `search_index.json` and the `pages/` directory.
- [ ] The script successfully outputs a structured `duplicates_report.json` or `duplicates_report.csv` file without crashing.
- [ ] The report clearly delineates between "Index Duplicates" (from `search_index.json`) and "File System Duplicates" (from the HTML folders).

## 2026-08-22T07:29:39Z

# Teamwork Project Prompt

Fix SEO issues to achieve 100/100 score and correct the broken home page link in all 238 country HTML pages without removing any existing data.

Working directory: C:\Users\recla\zipcode-global
Integrity mode: development

## Requirements

### R1. Fix Home Page Link
Update the home page link in all country HTML pages (e.g., `pages/india.html`) from `https://pozip.me/home/main.html` to the root domain `https://pozip.me/`. Ensure the replacement preserves surrounding layout and data.

### R2. Implement SEO "FIX" Items for Country Pages
Address the failing SEO checks on country pages (e.g., `india.html`):
1. **Title length & Alignment**: Adjust title tag and H1 to be aligned but not exact duplicates.
2. **Heading structure**: Ensure H2s break up content logically without skipping levels.
3. **Internal & External links**: Add relevant internal links and at least one credible external link.
4. **Image alt text**: Add descriptive alt text for important images.
5. **Canonical URL**: Add a self-referencing canonical tag.
6. **Social preview metadata**: Add Open Graph title, description, and image metadata.
7. **Breadcrumb schema**: Add BreadcrumbList schema.
8. **Definition support & Lists**: Add plain language definitions and bullet points.
9. **Original experience & Proof**: Add examples, data, or benchmarks.
10. **Organization/Entity schema**: Add WebPage, Organization, and disambiguation schema.

### R3. Safe Mass Patching
The repository contains over 180,000 files. Ensure any changes are applied efficiently (e.g., via a Python multiprocessing script) specifically targeting the 238 country HTML pages in the `pages` directory. **DO NOT REMOVE ANY EXISTING OLD DATA.**

## Acceptance Criteria

### Verification
- [ ] A Python script successfully modifies the 238 country HTML files in-place.
- [ ] Verification script confirms `https://pozip.me/home/main.html` no longer exists in any country page and is replaced by `https://pozip.me/`.
- [ ] Verification script confirms the presence of Open Graph tags and Canonical URL tags in `india.html`.
- [ ] Existing core content (word count, existing schema, data tables) remains intact without data loss.
