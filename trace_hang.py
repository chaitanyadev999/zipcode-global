import os
import sys

def main():
    pages_dir = "pages"
    count = 0
    with open("patch_trace.txt", "w", encoding="utf-8") as log:
        for root, dirs, files in os.walk(pages_dir):
            for file in files:
                if file.endswith(".html"):
                    count += 1
                    filepath = os.path.join(root, file)
                    log.write(f"{count}: {filepath}\n")
                    log.flush()
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        if 'seo-text' in content:
                            if '<div class="seo-text" style=" style="' in content:
                                pass
                    except Exception as e:
                        pass
    print("Done")

if __name__ == "__main__":
    main()
