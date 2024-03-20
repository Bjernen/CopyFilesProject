import shutil
import os

# Directory you wish to copy From.
direct_to_copy = "MainFolder"
# TARGET location of the backed up files.
destination_direct = "BackupFolder"

# Checks if target destination already exits.
os.makedirs(destination_direct, exist_ok=True)

files_and_dirs = os.listdir(direct_to_copy)
# Loop through items in the directory.
for name in files_and_dirs:
    # Combine the base directory ('direct_to_copy') with each item ('name') to form a full path.
    source_path = os.path.join(direct_to_copy, name)
    destination_path = os.path.join(destination_direct, name)

    # Checks if it is a file or a directory. If a directory it is required to use copytree().
    if os.path.isdir(source_path):
        # shutil.copytree for directories.
        try:
            shutil.copytree(source_path, destination_path)
        except FileExistsError as e:
            print(f"Directory {destination_path} already exists. Error: {e}")
    else:
        shutil.copy2(source_path, destination_path)  # Use shutil.copy2 for files.
