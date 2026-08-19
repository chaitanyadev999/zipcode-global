import os
import time

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
            # Read with retry
            content = None
            for _ in range(10):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    break
                except PermissionError:
                    time.sleep(0.1)
                    
            if content is None:
                errors += 1
                continue
                
            original_content = content

            if 'seo-text' in content:
                if start_str_broken in content:
                    start_idx = content.find(start_str_broken)
                    end_idx = content.find('>', start_idx)
                    if end_idx != -1:
                        old_tag = content[start_idx:end_idx+1]
                        content = content.replace(old_tag, new_div)
                
                elif start_str_details in content:
                    start_idx = content.find(start_str_details)
                    end_idx = content.find('>', start_idx)
                    if end_idx != -1:
                        old_tag = content[start_idx:end_idx+1]
                        content = content.replace(old_tag, new_div)
                    
                    sum_start = content.find('<summary')
                    if sum_start != -1:
                        sum_end = content.find('</summary>', sum_start)
                        if sum_end != -1:
                            content = content[:sum_start] + content[sum_end + 10:]
                    
                    if '</details>' in content:
                        content = content[::-1].replace('</details>'[::-1], '</div>'[::-1], 1)[::-1]
                
                if content != original_content:
                    # Write with retry
                    success = False
                    for _ in range(10):
                        try:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(content)
                            success = True
                            break
                        except PermissionError:
                            time.sleep(0.1)
                            
                    if success:
                        patched += 1
                    else:
                        errors += 1
                
        except Exception as e:
            errors += 1
            pass
            
        if (i + 1) % 10000 == 0:
            print(f"Processed {i + 1}/{total_files} files. Patched: {patched}. Errors: {errors}", flush=True)
            
    print(f"Done! Successfully patched {patched} files. Errors: {errors}", flush=True)

if __name__ == '__main__':
    main()
