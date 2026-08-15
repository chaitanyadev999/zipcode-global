import os
import re

files = [
    r"C:\Users\recla\zipcode-global\pages\about.html",
    r"C:\Users\recla\zipcode-global\pages\privacy.html",
    r"C:\Users\recla\zipcode-global\pages\report.html",
    r"C:\Users\recla\zipcode-global\pages\translate.html",
    r"C:\Users\recla\zipcode-global\pages\blog.html",
]

# Add blog posts
blog_dir = r"C:\Users\recla\zipcode-global\pages\blog"
for f in os.listdir(blog_dir):
    files.append(os.path.join(blog_dir, f))

# Also country-template.html maybe? Let's check it manually later.

correct_media = """@media(max-width:768px){
  .nav{flex-direction:column; gap:0.8rem; padding:0.8rem 1.25rem}
  .nav-links{flex-wrap:wrap; justify-content:center}
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove old bad media queries for .nav if they exist
    html = re.sub(r'@media\s*\(\s*max-width\s*:\s*768px\s*\)\s*\{\s*\.nav\s*\{[^}]+\}\s*\.nav-links\s*\{[^}]+\}\s*\}', '', html)
    
    # Now just inject the correct media query before </style>
    if correct_media not in html:
        html = html.replace('</style>', correct_media + "}\n</style>")
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated nav media queries in all auxiliary pages.")
