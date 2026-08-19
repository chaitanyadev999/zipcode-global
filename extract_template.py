with open('generate_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('HTML_TEMPLATE = r"""<!DOCTYPE html>')
if start != -1:
    end = text.find('"""', start + 25)
    with open('scratch_template.txt', 'w', encoding='utf-8') as f:
        f.write(text[start:end+3])
    print('Template extracted successfully to scratch_template.txt')
else:
    print('HTML_TEMPLATE not found')
