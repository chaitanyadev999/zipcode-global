import os

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
    
    new_div = '<div class="seo-text" style="max-height: 250px; overflow-y: auto;">'
    start_str_broken = '<div class="seo-text" style=" style="'
    start_str_details = '<details class="seo-text"'
    
    for i, filepath in enumerate(all_files):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            original_content = content

            if 'seo-text' in content:
                # 1. Handle broken double style div
                if start_str_broken in content:
                    start_idx = content.find(start_str_broken)
                    end_idx = content.find('>', start_idx)
                    if end_idx != -1:
                        old_tag = content[start_idx:end_idx+1]
                        content = content.replace(old_tag, new_div)
                
                # 2. Handle details tag
                elif start_str_details in content:
                    start_idx = content.find(start_str_details)
                    end_idx = content.find('>', start_idx)
                    if end_idx != -1:
                        old_tag = content[start_idx:end_idx+1]
                        content = content.replace(old_tag, new_div)
                    
                    # Remove summary tag (assumed to be closely following)
                    sum_start = content.find('<summary')
                    if sum_start != -1:
                        sum_end = content.find('</summary>', sum_start)
                        if sum_end != -1:
                            content = content[:sum_start] + content[sum_end + 10:]
                    
                    # Replace last </details> with </div>
                    if '</details>' in content:
                        content = content[::-1].replace('</details>'[::-1], '</div>'[::-1], 1)[::-1]
                
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
