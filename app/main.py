import tkinter as tk
import math

import config

number_of_buttons = len(config.rooms)
number_of_pages = math.ceil(number_of_buttons/3)

window = tk.Tk()

# Creates rows according to the number of rooms
# on the config file
for i in range(len(config.rooms)+1):
    window.rowconfigure(i, weight=1, minsize=75)
for i in range(2):
    window.columnconfigure(i, weight=1, minsize=120)

# Adds one button for each room on the config file
i = 0
for key in config.rooms.keys():
    tk.Button(master=window, text=key).grid(
        row=i,
        column=0,
        pady=1,
        sticky="nsew",
        columnspan=2
        )
    i += 1

# Adds the buttons to navigate between pages
btn_back = tk.Button(master=window, text="<<")
btn_back.grid(row=len(config.rooms), column=0, pady=1, sticky="nsew")
btn_fwd = tk.Button(master=window, text=">>")
btn_fwd.grid(row=len(config.rooms), column=1, pady=1, sticky="nsew")

window.mainloop()
