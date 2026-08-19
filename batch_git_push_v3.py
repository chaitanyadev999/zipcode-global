import subprocess
import time
import math
import os

def run_cmd(cmd_list):
    print(f"Running: {' '.join(cmd_list)}", flush=True)
    subprocess.run(cmd_list, check=True)

def main():
    print("Getting list of modified files...", flush=True)
    result = subprocess.run("git ls-files --modified", shell=True, capture_output=True, text=True)
    files = [f for f in result.stdout.split('\n') if f.strip()]
    
    if not files:
        print("Checking untracked files...", flush=True)
        result = subprocess.run("git ls-files --others --exclude-standard", shell=True, capture_output=True, text=True)
        files = [f for f in result.stdout.split('\n') if f.strip()]
        
    print(f"Found {len(files)} files to commit.", flush=True)
    
    batch_size = 20000
    total_batches = math.ceil(len(files) / batch_size)
    
    for i in range(total_batches):
        batch = files[i * batch_size : (i + 1) * batch_size]
        print(f"\n--- Processing Batch {i+1}/{total_batches} ({len(batch)} files) ---", flush=True)
        
        # Write paths to a file and use pathspec-from-file to avoid command line limits and shell issues
        with open("paths_to_add.txt", "w", encoding="utf-8") as f:
            for filepath in batch:
                f.write(filepath + "\n")
                
        print("Adding files...", flush=True)
        run_cmd(['git', 'add', '--pathspec-from-file=paths_to_add.txt'])
                
        # Commit
        print("Committing...", flush=True)
        run_cmd(['git', 'commit', '-m', f"feat: SEO update batch {i+1} of {total_batches}"])
        
        # Push
        print("Pushing to remote...", flush=True)
        try:
            run_cmd(['git', 'push'])
            print(f"Successfully pushed batch {i+1}", flush=True)
        except Exception as e:
            print(f"Failed to push batch {i+1}, retrying in 5 seconds...", flush=True)
            time.sleep(5)
            run_cmd(['git', 'push'])
            
        time.sleep(2)
        
    if os.path.exists("paths_to_add.txt"):
        os.remove("paths_to_add.txt")
    print("\nAll batches successfully committed and pushed!", flush=True)

if __name__ == "__main__":
    main()
