with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    
# Remove the broken top summary bar
broken_bar = '''<!-- TOP SUMMARY FOR SEO/AEO -->
<div class="top-summary-bar" style="background: rgba(0, 212, 255, 0.05); border-bottom: 1px solid rgba(0, 212, 255, 0.1); padding: 8px 15px; text-align: center; font-size: 0.85rem; color: var(--t2);">
  <strong style="color: var(--cyan);">Top Summary:</strong> The ultimate directory to instantly verify and search accurate postal codes, ZIP codes, and PIN codes for 121+ countries worldwide.
</div>'''

if broken_bar in text:
    text = text.replace(broken_bar + '\n', '')
    text = text.replace(broken_bar, '')
    print('Removed broken top summary bar')
else:
    print('Broken top summary bar not found')

# Add the sr-only summary right after the H1
h1_text = '<h1>Find <span class="grad-text">Postal & ZIP Codes</span> for 121+ Countries</h1>'
sr_only_summary = '''
<!-- SEO Hidden Summaries (Screen Reader Only) -->
<div style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;">
  <strong>Top Summary:</strong> The ultimate directory to instantly verify and search accurate postal codes, ZIP codes, and PIN codes for 121+ countries worldwide.
  <strong>Bottom Line:</strong> Get instant access to millions of ZIP and PIN codes updated live.
</div>
'''

if h1_text in text and 'SEO Hidden Summaries' not in text:
    text = text.replace(h1_text, h1_text + sr_only_summary)
    print('Added sr-only SEO summaries')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
