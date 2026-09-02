import os
import concurrent.futures

pages_dir = r"C:\Users\recla\zipcode-global\pages"
favicon_tag = '<link rel="icon" type="image/png" href="/home/assets/logo.png">\n'

def patch_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<link rel="icon"' not in content:
            if '<head>\n' in content:
                content = content.replace('<head>\n', '<head>\n' + favicon_tag)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                return 1
            elif '<head>' in content:
                content = content.replace('<head>', '<head>\n' + favicon_tag)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                return 1
    except Exception as e:
        pass
    return 0

if __name__ == '__main__':
    all_files = []
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.html'):
                all_files.append(os.path.join(root, file))
    
    print(f"Found {len(all_files)} html files. Patching...")
    
    count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        results = executor.map(patch_file, all_files)
        for r in results:
            count += r
            
    print(f"Added favicon to {count} files.")
