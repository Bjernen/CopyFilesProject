import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Backup Program")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="Nødvendig Information: ")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text="Backup fra:")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Backup til:")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Saml backup i .zip fil?")
title_combobox = ttk.Combobox(user_info_frame, values=["Ja", "Nej"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


window.mainloop()
