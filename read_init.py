with open('generate_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('window.addEventListener(\'scroll\'')
print(text[start-100:start+300])
