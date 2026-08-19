import subprocess
import time
import math

def run_cmd(cmd):
    print(f"Running: {cmd}", flush=True)
    subprocess.run(cmd, shell=True, check=True)

def main():
    print("Getting list of modified files...", flush=True)
    result = subprocess.run("git ls-files --modified", shell=True, capture_output=True, text=True)
    files = [f for f in result.stdout.split('\n') if f.strip()]
    
    if not files:
        # Maybe they are untracked?
        print("Checking untracked files...", flush=True)
        result = subprocess.run("git ls-files --others --exclude-standard", shell=True, capture_output=True, text=True)
        files = [f for f in result.stdout.split('\n') if f.strip()]
        
    print(f"Found {len(files)} files to commit.", flush=True)
    
    batch_size = 20000
    total_batches = math.ceil(len(files) / batch_size)
    
    for i in range(total_batches):
        batch = files[i * batch_size : (i + 1) * batch_size]
        print(f"\n--- Processing Batch {i+1}/{total_batches} ({len(batch)} files) ---", flush=True)
        
        # Write batch files to a text file for git to read
        with open("batch_files.txt", "w", encoding="utf-8") as f:
            for filepath in batch:
                f.write(filepath + "\n")
                
        # Add files from the text file
        print("Adding files to git...", flush=True)
        run_cmd("git update-index --add --stdin < batch_files.txt")
        
        # Commit
        print("Committing...", flush=True)
        run_cmd(f"git commit -m \"feat: SEO update batch {i+1} of {total_batches}\"")
        
        # Push
        print("Pushing to remote...", flush=True)
        try:
            run_cmd("git push")
            print(f"Successfully pushed batch {i+1}", flush=True)
        except Exception as e:
            print(f"Failed to push batch {i+1}, retrying in 5 seconds...", flush=True)
            time.sleep(5)
            run_cmd("git push")
            
        time.sleep(2)
        
    print("\nAll batches successfully committed and pushed!", flush=True)

if __name__ == "__main__":
    main()
