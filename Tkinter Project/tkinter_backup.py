import tkinter # Used to create the GUI
from tkinter import ttk
from tkinter import messagebox
import os
import shutil # Offers support for copying and moving files
from tkinter.filedialog import askdirectory  # Allows the user to click a button to specify location and destination.


# Function for the backup process.
def backup_files():
    direct_to_copy = backup_dir_var.get()
    destination_directory = destination_dir_var.get()
    zip_backup = title_combobox.get()

    # Validate input
    if not direct_to_copy or not destination_directory:
        messagebox.showwarning("Warning", "Fill in both directories.")
        return
    try:
        # Check if target destination already exists, and create it if not.
        os.makedirs(destination_directory, exist_ok=True)

        files_and_dirs = os.listdir(direct_to_copy)

        for name in files_and_dirs:
            source_path = os.path.join(direct_to_copy, name)
            destination_path = os.path.join(destination_directory, name)
            if os.path.isdir(source_path):
                # Using shutil.copytree for directories.
                try:
                    shutil.copytree(source_path, destination_path)
                except FileExistsError:
                    print(f"\nWARNING: Directory {destination_path} already exists.")
            else:
                # shutil.copy2 for copying files.
                shutil.copy2(source_path, destination_path)
        # If 'Yes' is selected to zip the file.
        if zip_backup == "Yes":
            shutil.make_archive(destination_directory, 'zip', destination_directory)
            messagebox.showinfo("Success", f"Backup saved and zipped: {destination_directory}.zip")
        else:
            messagebox.showinfo("Success", f"Backup saved to: {destination_directory}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to backup files. Error: {e}")


# Function to select the backup source directory and update the label.
def select_backup_directory():
    directory = askdirectory()
    if directory:  # Check if a directory was selected.
        backup_dir_var.set(directory)


# Function to select the backup destination directory and update the label.
def select_destination_directory():
    directory = askdirectory()
    if directory:  # Check if a directory was selected.
        destination_dir_var.set(directory)


# Setup for the tkinter window.
window = tkinter.Tk()
window.title("Official Backup Program of Deep Space 9 - Made by Quark!")

frame = tkinter.Frame(window)
frame.pack()

# User Info Frame.
user_info_frame = tkinter.LabelFrame(frame, text="Required Information: ")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

# Variables to hold the directory paths.
backup_dir_var = tkinter.StringVar()
destination_dir_var = tkinter.StringVar()

# Select Backup Directory button and label.
select_backup_button = tkinter.Button(user_info_frame, text="Select Backup Directory", command=select_backup_directory)
select_backup_button.grid(row=0, column=0)
backup_dir_label = tkinter.Label(user_info_frame, textvariable=backup_dir_var)
backup_dir_label.grid(row=1, column=0)

# Select Destination Directory button and label.
select_destination_button = tkinter.Button(user_info_frame, text="Select Destination Directory",
                                           command=select_destination_directory)
select_destination_button.grid(row=0, column=1)
destination_dir_label = tkinter.Label(user_info_frame, textvariable=destination_dir_var)
destination_dir_label.grid(row=1, column=1)

# Zip backup option
title_label = tkinter.Label(user_info_frame, text="Save backup in a .zip file?")
title_label.grid(row=2, column=0)
title_combobox = ttk.Combobox(user_info_frame, values=["Yes", "No"])
title_combobox.grid(row=3, column=0)
title_combobox.set("No")

# Backup button
backup_button = tkinter.Button(frame, text="Engage!", command=backup_files)
backup_button.grid(row=2, column=0, pady=20)

# Adjust padding for all child widgets.
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=50, pady=5)


window.mainloop()
