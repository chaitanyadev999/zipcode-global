import subprocess

out = subprocess.check_output(['git', 'status', '--porcelain']).decode('utf-8')
files = [line.strip()[2:].strip() for line in out.splitlines() if line.strip().startswith('M ') or line.strip().startswith('A ')]

batch_size = 30000
for i in range(0, len(files), batch_size):
    batch = files[i:i+batch_size]
    print(f"Processing batch {i//batch_size + 1} of {len(files)//batch_size + 1}...")
    
    chunk_size = 500
    for j in range(0, len(batch), chunk_size):
        subprocess.run(['git', 'add'] + batch[j:j+chunk_size])
        
    subprocess.run(['git', 'commit', '-m', f"SEO: Add favicon (batch {i//batch_size + 1})"])
    
    res = subprocess.run(['git', 'push'])
    if res.returncode != 0:
        print("Push failed, retrying...")
        subprocess.run(['git', 'push'])
