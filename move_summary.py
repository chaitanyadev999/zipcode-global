import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

summary_match = re.search(r'<!-- AEO / GEO Top Summary -->.*?</div>', content, flags=re.DOTALL)
if summary_match:
    summary_block = summary_match.group(0)
    # Remove from current location
    content = content.replace(summary_block, '')
    
    # Inject below the finder-wrapper completely.
    # Look for the ending </div> of finder-wrapper. It's right after <div id="finderResult"...></div>
    content = re.sub(r'(<div id="finderResult".*?</div>\s*</div>)', r'\1\n\n' + summary_block, content, count=1, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Moved Top Summary successfully.')
else:
    print('Top Summary not found.')
