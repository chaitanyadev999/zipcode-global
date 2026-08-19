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
    
    for i, filepath in enumerate(all_files):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            original_content = content

            if '<details class="seo-text"' in content or 'style=" style="' in content:
                # Fix double style error if it exists, or replace details if it hasn't been replaced
                content = re.sub(r'<details class="seo-text".*?>', r'<div class="seo-text" style="max-height: 250px; overflow-y: auto;">', content, count=1)
                content = re.sub(r'<div class="seo-text" style=" style=".*?>', r'<div class="seo-text" style="max-height: 250px; overflow-y: auto;">', content, count=1)
                
                # Remove summary
                content = re.sub(r'<summary.*?>.*?</summary>', '', content, count=1, flags=re.DOTALL)
                
                # Replace the last </details> (which should be ours)
                if '</details>' in content:
                    content = content[::-1].replace('</details>'[::-1], '</div>'[::-1], 1)[::-1]
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    patched += 1
                
        except Exception as e:
            errors += 1
            pass
            
        if (i + 1) % 5000 == 0:
            print(f"Processed {i + 1}/{total_files} files. Patched: {patched}. Errors: {errors}", flush=True)
            
    print(f"Done! Successfully patched {patched} files.", flush=True)

if __name__ == '__main__':
    main()
