import re

content = '<div class="seo-text" style=" style="padding: 20px; background: rgba(255,255,255,0.05); margin: 20px auto; max-width: 800px; border-radius: 8px; color: #ccc; line-height: 1.6; text-align: center; font-size: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); cursor: pointer;"; max-height: 250px; overflow-y: auto;">'

print("Original:")
print(content)

new_content = re.sub(r'<div class="seo-text" style=" style=".*?>', r'<div class="seo-text" style="max-height: 250px; overflow-y: auto;">', content, count=1)

print("\nReplaced:")
print(new_content)
