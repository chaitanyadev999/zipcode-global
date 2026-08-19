import re

with open('pages/india.html', 'r', encoding='utf-8') as f:
    text = f.read()

    # Find search input
    for line in text.split('\n'):
        if 'type="text"' in line or 'type="search"' in line:
            print("Input:", line.strip())

    # Find event listeners
    print("\nListeners:")
    for line in text.split('\n'):
        if 'addEventListener' in line and 'search' in line.lower():
            print(line.strip())
