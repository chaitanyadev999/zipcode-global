import os

filepath = r"C:\Users\recla\zipcode-global\pages\about.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Add a CSS block for the new grid layout
grid_css = """
        /* ABOUT GRID */
        .about-grid-wrapper { display: flex; gap: 40px; align-items: flex-start; margin-bottom: 40px; flex-wrap: wrap; }
        .about-grid-content { flex: 1 1 500px; display: flex; flex-direction: column; gap: 30px; }
        .about-grid-image { flex: 1 1 300px; position: sticky; top: 100px; }
        .about-grid-image img { width: 100%; border-radius: 16px; border: 1px solid rgba(0,212,255,0.2); box-shadow: 0 0 30px rgba(0,212,255,0.15); }
"""
html = html.replace('/* MADE WITH LOVE OF EARTH */', grid_css + '\n        /* MADE WITH LOVE OF EARTH */')

# Find the start and end of the sections to wrap
start_idx = html.find('<!-- WHAT IS -->')
end_idx = html.find('<!-- MADE WITH LOVE OF EARTH -->')
# Backup just in case
with open(filepath + ".bak", 'w', encoding='utf-8') as f: f.write(html)

if start_idx != -1 and end_idx != -1:
    before = html[:start_idx]
    
    # We want to wrap the sections up to the hr
    hr_idx = html.rfind('<hr class="section-divider">', start_idx, end_idx)
    
    middle = html[start_idx:hr_idx]
    after = html[hr_idx:]
    
    new_middle = f"""<div class="about-grid-wrapper">
    <div class="about-grid-content">
{middle}
    </div>
    <div class="about-grid-image">
        <img src="/home/assets/about_side.png" alt="PO ZipCode Global World Map">
    </div>
</div>
"""
    
    html = before + new_middle + after
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated about.html successfully!")
else:
    print("Could not find sections.")

