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
