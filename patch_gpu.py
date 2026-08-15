import re

# PATCH shared_pseo.css
with open('pages/shared_pseo.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. hero-flag
css = re.sub(
    r'(animation:\s*flag-float[^;]+;)\s*\}',
    r'\1\n  will-change: transform;\n  transform: translateZ(0);\n}',
    css
)
css = css.replace('transform: translateY(0);', 'transform: translateY(0) translateZ(0);')
css = css.replace('transform: translateY(-8px);', 'transform: translateY(-8px) translateZ(0);')

# 2. search-btn
css = re.sub(
    r'(transition:\s*all var\(--d-fast\) var\(--ease-out\);)\s*\}',
    r'\1\n  will-change: transform;\n}',
    css, count=1 # Only first one or we can just replace specifically
)
css = css.replace('transform: scale(1.05);', 'transform: scale(1.05) translateZ(0);')

# 3. state-btn
css = css.replace('transform: translateY(-2px);', 'transform: translateY(-2px) translateZ(0);')
# to add will-change to state-btn, find it
css = re.sub(
    r'(\.state-btn\s*\{[^}]*transition:\s*all var\(--d-fast\) var\(--ease-out\);)\s*\}',
    r'\1\n  will-change: transform;\n}',
    css
)

# 4. map-section and results-section
css = re.sub(
    r'(\.map-section\s*\{[^}]*transition:\s*all[^;]+;)\s*max-height: 0;',
    r'\1\n  will-change: transform, opacity;\n  max-height: 0;',
    css
)
css = re.sub(
    r'(\.results-section\s*\{[^}]*transition:\s*all[^;]+;)\s*max-height: 0;',
    r'\1\n  will-change: transform, opacity;\n  max-height: 0;',
    css
)

# 5. result-card
css = re.sub(
    r'(\.result-card\s*\{[^}]*opacity: 0;\s*transform:\s*translateY\(20px\);)\s*\}',
    r'\1\n  will-change: transform, opacity;\n}',
    css
)
css = css.replace('transform: translateY(-4px);', 'transform: translateY(-4px) translateZ(0);')

# 6. spinner
css = re.sub(
    r'(\.spinner\s*\{[^}]*margin: 0 auto 1rem;)\s*\}',
    r'\1\n  will-change: transform;\n  transform: translateZ(0);\n}',
    css
)
css = css.replace('transform: rotate(360deg);', 'transform: rotate(360deg) translateZ(0);')

# 7. toast
css = re.sub(
    r'(\.toast\s*\{[^}]*transition:\s*transform[^;]+;)\s*box-shadow:',
    r'\1\n  will-change: transform;\n  box-shadow:',
    css
)
css = css.replace('transform: translateX(0);', 'transform: translateX(0) translateZ(0);')

with open('pages/shared_pseo.css', 'w', encoding='utf-8') as f:
    f.write(css)

# PATCH home/main.html
with open('home/main.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('transform:translateY(0)', 'transform:translateY(0) translateZ(0)')
html = html.replace('transform:translateY(-8px)', 'transform:translateY(-8px) translateZ(0)')
html = html.replace('transform:translateX(0)', 'transform:translateX(0) translateZ(0)')
html = html.replace('transform:translateX(-100%)', 'transform:translateX(-100%) translateZ(0)')
html = html.replace('transform: translateX(0)', 'transform: translateX(0) translateZ(0)')
html = html.replace('transform: translateX(-50%)', 'transform: translateX(-50%) translateZ(0)')
html = html.replace('transform:translateY(-12px) scale(1.1)', 'transform:translateY(-12px) scale(1.1) translateZ(0)')
html = html.replace('transform:scale(1)', 'transform:scale(1) translateZ(0)')

html = re.sub(
    r'(\.toast\s*\{[^}]*transition:transform[^;]+;)\s*\}',
    r'\1\n  will-change: transform;\n}',
    html
)
html = re.sub(
    r'(\.pcard\s*\{[^}]*transition:all[^;]+;)\s*display:flex;',
    r'\1\n  will-change: transform;\n  display:flex;',
    html
)
html = re.sub(
    r'(\.citem\s*\{[^}]*transition:all[^;]+;)\s*text-decoration:none;',
    r'\1\n  will-change: transform;\n  text-decoration:none;',
    html
)

with open('home/main.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Patched successfully")
