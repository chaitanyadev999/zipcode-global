
import os, glob

pages_dir = "pages"

for filepath in glob.glob(os.path.join(pages_dir, "*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. showPins signature
    content = content.replace("function showPins(records){", "function showPins(records, autoScroll=true){")
    
    # 2. autoScroll condition
    if "if(autoScroll) $(\x27s3\x27).scrollIntoView" not in content:
        content = content.replace("$(\x27s3\x27).scrollIntoView({behavior:\x27smooth\x27,block:\x27start\x27});", "if(autoScroll) $(\x27s3\x27).scrollIntoView({behavior:\x27smooth\x27,block:\x27start\x27});")

    # 3. doSearch signature
    content = content.replace("async function doSearch(){", "async function doSearch(isManual=false){")

    # 4. showPins inside doSearch (this is the only place it is `showPins(hits);`)
    content = content.replace("showPins(hits);", "showPins(hits, isManual);")

    # 5. onclick="doSearch()"
    content = content.replace("onclick=\"doSearch()\"", "onclick=\"doSearch(true)\"")

    # 6. enter keypress
    content = content.replace("if(e.key===\x27Enter\x27)doSearch();});", "if(e.key===\x27Enter\x27)doSearch(true);});")

    # 7. input auto search
    content = content.replace("searchTo=setTimeout(doSearch,400);});", "searchTo=setTimeout(()=>doSearch(false),400);});")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
print("Done patching.")
