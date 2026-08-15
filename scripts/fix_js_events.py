import os

pages_dir = r"C:\Users\recla\zipcode-global\pages"
updated = 0

for file in os.listdir(pages_dir):
    if not file.endswith('.html'): continue
    
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    orig_html = html
    
    # Fix the event.currentTarget throwing ReferenceError
    html = html.replace("if (event && event.currentTarget)", "if (window.event && window.event.currentTarget)")
    html = html.replace("event.currentTarget.classList.add('active')", "window.event.currentTarget.classList.add('active')")
    
    # Fix window.selectState in the search function
    html = html.replace("await window.selectState(", "await selectState(")
    
    # In selectState, some browsers might still complain if window.event isn't available. We can do:
    # try{ if(window.event && window.event.currentTarget) window.event.currentTarget.classList.add('active'); }catch(e){}
    # But window.event check is safe.
    
    if html != orig_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        updated += 1

print(f"Updated {updated} files with JS event fixes.")
