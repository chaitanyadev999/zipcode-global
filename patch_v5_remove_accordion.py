import os
import multiprocessing
import re

def process_chunk(file_paths):
    count = 0
    for filepath in file_paths:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # We need to change <details class="seo-text"...> to <div class="seo-text"...>
            # and </details> to </div>.
            # But ONLY for the seo-text block.
            
            if '<details class="seo-text"' in content:
                # Replace the opening tag
                content = re.sub(r'<details class="seo-text"(.*?)>', r'<div class="seo-text" style="\1; max-height: 250px; overflow-y: auto;">', content, count=1)
                
                # Replace the closing tag. The closing tag is right before </body> usually.
                # To be safe, we replace the LAST </details> in the file.
                # Or just use regex to replace </details> right after the seo text.
                
                # Actually, the summary tag needs to be removed too.
                content = re.sub(r'<summary.*?>.*?</summary>', '', content, count=1, flags=re.DOTALL)
                
                # Replace the FIRST </details> that appears after our div
                content = content.replace('</details>', '</div>', 1)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                
        except Exception as e:
            pass
    return count

def main():
    print("Gathering HTML files...")
    all_files = []
    pages_dir = os.path.join("pages", "india")
    
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith(".html"):
                all_files.append(os.path.join(root, file))
                
    print(f"Found {len(all_files)} files. Patching back to DIV with scrollbar...")
    
    # Process in chunks
    chunk_size = 5000
    chunks = [all_files[i:i + chunk_size] for i in range(0, len(all_files), chunk_size)]
    
    total_patched = 0
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        for result in pool.imap_unordered(process_chunk, chunks):
            total_patched += result
            print(f"Patched {total_patched}/{len(all_files)} files...")
            
    print("Done patching! Now you can run the git batch script.")

if __name__ == '__main__':
    # Add windows multiprocessing support freeze_support
    multiprocessing.freeze_support()
    main()
