import os
import re

def main():
    print("Gathering HTML files...", flush=True)
    all_files = []
    pages_dir = "pages"
    
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith(".html"):
                all_files.append(os.path.join(root, file))
                
    total_files = len(all_files)
    print(f"Found {total_files} files. Patching...", flush=True)
    
    patched = 0
    errors = 0
    
    # Pre-compile regex for speed
    re_details_open = re.compile(r'<details class="seo-text".*?>')
    re_summary = re.compile(r'<summary.*?>.*?</summary>', re.DOTALL)
    re_div_broken = re.compile(r'<div class="seo-text" style=" style=".*?>')
    
    for i, filepath in enumerate(all_files):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            original_content = content

            if 'seo-text' in content:
                # 1. If it has a details tag, replace it
                if '<details class="seo-text"' in content:
                    content = re_details_open.sub('<div class="seo-text" style="max-height: 250px; overflow-y: auto;">', content, count=1)
                    content = re_summary.sub('', content, count=1)
                    if '</details>' in content:
                        content = content[::-1].replace('</details>'[::-1], '</div>'[::-1], 1)[::-1]
                
                # 2. If it has the broken double style div, replace it
                elif 'style=" style="' in content:
                    content = re_div_broken.sub('<div class="seo-text" style="max-height: 250px; overflow-y: auto;">', content, count=1)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    patched += 1
                
        except Exception as e:
            errors += 1
            pass
            
        if (i + 1) % 10000 == 0:
            print(f"Processed {i + 1}/{total_files} files. Patched: {patched}. Errors: {errors}", flush=True)
            
    print(f"Done! Successfully patched {patched} files.", flush=True)

if __name__ == '__main__':
    main()
