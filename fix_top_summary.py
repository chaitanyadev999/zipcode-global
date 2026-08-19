with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove the old Bottom Line box I added at the bottom
old_box = '''<!-- BOTTOM LINE SEO SUMMARY -->
<div style="max-width:900px; margin:-10px auto 40px auto; text-align:center; padding:0 15px;">
  <p style="color:var(--t3); font-size:1rem; font-style:italic;">
    <strong style="color:var(--cyan); font-style:normal;">Bottom Line:</strong> Instantly verify and search accurate postal codes, ZIP codes, and PIN codes for over 121 countries globally.
  </p>
</div>'''

if old_box in text:
    text = text.replace(old_box + '\n', '')
    text = text.replace(old_box, '')
    print('Removed old Bottom Line box')
else:
    print('Old Bottom Line box not found')

# 2. Insert the announcement bar right after <div class="toast-wrap" id="toastWrap"></div>
announcement = '''
<!-- TOP SUMMARY FOR SEO/AEO -->
<div class="top-summary-bar" style="background: rgba(0, 212, 255, 0.05); border-bottom: 1px solid rgba(0, 212, 255, 0.1); padding: 8px 15px; text-align: center; font-size: 0.85rem; color: var(--t2);">
  <strong style="color: var(--cyan);">Top Summary:</strong> The ultimate directory to instantly verify and search accurate postal codes, ZIP codes, and PIN codes for 121+ countries worldwide.
</div>
'''

target = '<div class="toast-wrap" id="toastWrap"></div>\n'
if target in text:
    text = text.replace(target, target + announcement)
    print('Added announcement bar at the top')
else:
    print('Toast wrap not found')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
