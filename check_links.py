import os, glob, re

def check():
    file1 = glob.glob('pages/*/*.html')
    if file1:
        with open(file1[0], 'r', encoding='utf-8') as f:
            content = f.read()
            print("File:", file1[0])
            for m in re.findall(r'href=[\"\'](.*?)[\"\']', content):
                print(m)
            
            nav_matches = re.findall(r'<nav.*?</nav>', content, re.DOTALL)
            if not nav_matches:
                print("No <nav> tag found. Maybe it's injected by JS?")
                
            js_includes = re.findall(r'<script.*?src=[\"\'](.*?)[\"\']', content)
            print("JS:", js_includes)

check()
