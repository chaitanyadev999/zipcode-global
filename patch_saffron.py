import os

files = [
    r'C:\Users\recla\zipcode-global\pages\about.html',
    r'C:\Users\recla\zipcode-global\pages\privacy.html',
    r'C:\Users\recla\zipcode-global\pages\report.html'
]

for file_path in files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace specific old orange variables with standard ones
    content = content.replace('var(--saffron)', 'var(--p)')
    content = content.replace('var(--gold)', 'var(--a)')
    content = content.replace('255, 107, 26', 'var(--p2-rgb)')
    content = content.replace('255,107,26', 'var(--p2-rgb)')
    
    # Optional cleanup of redundant root definitions
    # It might be fine to leave them since they won't be used anymore, but better if we clean it.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {file_path}")

