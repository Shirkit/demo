import torch
import torch.nn as nn
import os
import time

def run_experiment():
    print("--- Starting Lab Experiment ---")
    
    # 1. Verify Hardware
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    if torch.cuda.is_available():
        print(f"GPU Name: {torch.cuda.get_device_name(0)}")
        print(f"Total VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")

    # 2. Dummy "Training" Task
    # We create a large matrix multiplication to put some load on the GPU/CPU
    print("Running matrix multiplication task...")
    x = torch.randn(2000, 2000).to(device)
    y = torch.randn(2000, 2000).to(device)
    start_time = time.time()
    
    for _ in range(100):
        res = torch.matmul(x, y)
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Task completed in {duration:.4f} seconds.")

    # 3. Save Persistent Results
    # This folder is mapped to the server's hard drive via Slurm/Docker
    results_path = "/app/results/summary.txt"
    
    with open(results_path, "w") as f:
        f.write(f"Experiment Results\n")
        f.write(f"Device used: {device}\n")
        f.write(f"Computation time: {duration:.4f} seconds\n")
        f.write(f"Status: SUCCESS\n")
    
    print(f"Results saved to {results_path}")

if __name__ == "__main__":
    run_experiment()
