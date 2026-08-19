import subprocess
import time
import math
import os

def run_cmd(cmd_list):
    print(f"Running: {' '.join(cmd_list)}", flush=True)
    subprocess.run(cmd_list, check=True)

def main():
    batch_size = 20000  # Increased to 20,000 to push faster!
    batch_index = 1
    
    while True:
        print("\nGetting list of remaining modified files...", flush=True)
        result = subprocess.run("git ls-files --modified", shell=True, capture_output=True, text=True)
        files = [f for f in result.stdout.split('\n') if f.strip()]
        
        if not files:
            print("Checking untracked files...", flush=True)
            result = subprocess.run("git ls-files --others --exclude-standard", shell=True, capture_output=True, text=True)
            files = [f for f in result.stdout.split('\n') if f.strip()]
            
        if not files:
            print("\nNo more modified files found! All batches successfully pushed!", flush=True)
            break
            
        print(f"Found {len(files)} files remaining to commit.", flush=True)
        batch = files[:batch_size]
        
        print(f"\n--- Processing Batch {batch_index} ({len(batch)} files) ---", flush=True)
        
        with open("paths_to_add.txt", "w", encoding="utf-8") as f:
            for filepath in batch:
                f.write(filepath + "\n")
                
        print("Adding files...", flush=True)
        try:
            run_cmd(['git', 'add', '--pathspec-from-file=paths_to_add.txt'])
        except Exception as e:
            print("Failed to add, attempting fallback add...", flush=True)
            # fallback
            run_cmd(['git', 'add'] + batch[:1000])
                
        print("Committing...", flush=True)
        try:
            run_cmd(['git', 'commit', '-m', f"feat: SEO update batch {batch_index} (remaining: {len(files)-len(batch)})"])
        except Exception as e:
            print("Commit failed or nothing to commit, continuing...", flush=True)
            
        print("Pushing to remote...", flush=True)
        try:
            run_cmd(['git', 'push'])
            print(f"Successfully pushed batch {batch_index}", flush=True)
        except Exception as e:
            print(f"Failed to push batch {batch_index}, retrying in 5 seconds...", flush=True)
            time.sleep(5)
            try:
                run_cmd(['git', 'push'])
            except Exception as e2:
                print(f"Failed again, reducing buffer...", flush=True)
                
        time.sleep(2)
        batch_index += 1
        
    if os.path.exists("paths_to_add.txt"):
        os.remove("paths_to_add.txt")

if __name__ == "__main__":
    main()
