import os
import glob
import shutil
import re

# 1. Copy generated images to the assets/blog/ directory
source_dir = r"C:\Users\recla\.gemini\antigravity\brain\2a8e2121-bbe9-4c45-b6d3-34eed8ac51fe"
dest_dir = r"C:\Users\recla\zipcode-global\home\assets\blog"

os.makedirs(dest_dir, exist_ok=True)

# Find all generated images
img_files = glob.glob(os.path.join(source_dir, "img_*.png"))

# Map the images 1 to 13 to standardized names
img_map = {}
for img in img_files:
    basename = os.path.basename(img)
    # Extract the number from 'img_1_india_pin_1786023338844.png'
    match = re.search(r'img_(\d+)_', basename)
    if match:
        num = int(match.group(1))
        new_name = f"ai_cover_{num}.png"
        shutil.copy2(img, os.path.join(dest_dir, new_name))
        img_map[num] = new_name

# For 14 and 15 (which failed due to quota), we'll reuse some other images to keep the AI look
if 4 in img_map:
    shutil.copy2(os.path.join(dest_dir, img_map[4]), os.path.join(dest_dir, "ai_cover_14.png"))
if 7 in img_map:
    shutil.copy2(os.path.join(dest_dir, img_map[7]), os.path.join(dest_dir, "ai_cover_15.png"))

# 2. Update blog.html to use these new images
blog_path = r'C:\Users\recla\zipcode-global\pages\blog.html'
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_html = f.read()

count = 1
def replace_img(match):
    global count
    res = f'<img src="/home/assets/blog/ai_cover_{count}.png"'
    count += 1
    return res

# The previous script replaced them with picsum urls
blog_html = re.sub(r'<img src="https://picsum.photos/600/400\?random=\d+"', replace_img, blog_html)

with open(blog_path, 'w', encoding='utf-8') as f:
    f.write(blog_html)

print("Images copied and blog.html updated successfully!")
