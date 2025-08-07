import os
import shutil

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "ncbi_dataset", "data")
output_dir = os.path.join(current_dir, "all_fastas")

os.makedirs(output_dir, exist_ok=True)

for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(".fna"):
            full_path = os.path.join(root, file)
            new_filename = os.path.basename(file)
            shutil.copy(full_path, os.path.join(output_dir, new_filename))

print("All .fna files copied to:", output_dir)
