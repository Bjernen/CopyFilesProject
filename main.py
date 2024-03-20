# Import shutil(2) module - This module preservers metadata
import shutil
# from pathlib import Path
import os


# Directory you wish to copy From.
direct_to_copy = "MainFolder"
# TARGET location of the backed up files.
destination_direct = "BackupFolder"

files = os.listdir(direct_to_copy)
# For loop which copies all files in a folder.
for fname in files:
    shutil.copy2(os.path.join(direct_to_copy, fname), destination_direct)

