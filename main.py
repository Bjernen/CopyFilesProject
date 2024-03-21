# Import shutil, and use shutil.copy2 to copy files as it also copies metadata.
import shutil
import os

# Directory to copy from.
config_file_path = "config_file.txt"


with open(config_file_path, "r") as file:
    lines = file.readlines()
    direct_to_copy = lines[0].strip()
    destination_directory = lines[1].strip()

# Check if target destination already exits.
os.makedirs(destination_directory, exist_ok=True)

files_and_dirs = os.listdir(direct_to_copy)
# Loop through items in the directory.
for name in files_and_dirs:
    # Combine main directory ('direct_to_copy') with each item ('name') to form a full path.
    source_path = os.path.join(direct_to_copy, name)
    destination_path = os.path.join(destination_directory, name)
    print(f"Creating Backup of.... {name}")

    # Checks if it is a file or a directory. If a directory it is required to use copytree().
    if os.path.isdir(source_path):
        # shutil.copytree for directories.
        try:
            shutil.copytree(source_path, destination_path)
        except FileExistsError:
            print(f"\nWARNING : Directory {destination_path} already exists.")
    else:
        shutil.copy2(source_path, destination_path)  # Use shutil.copy2 for files.

print(f"Saving Backup To: {destination_directory}")
print("\n----Backup Completed!----")