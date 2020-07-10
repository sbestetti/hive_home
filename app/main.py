import tkinter as tk

window = tk.Tk()

for i in range(4):
    window.rowconfigure(i, weight=1, minsize=75)

for i in range(2):
    window.columnconfigure(i, weight=1, minsize=120)

btn_1 = tk.Button(master=window, text="Quarto")
btn_1.grid(row=0, column=0, pady=1, sticky="nsew", columnspan=2)

btn_2 = tk.Button(master=window, text="Banheiro")
btn_2.grid(row=1, column=0, pady=1, sticky="nsew", columnspan=2)

btn_3 = tk.Button(master=window, text="Corredor")
btn_3.grid(row=2, column=0, pady=1, sticky="nsew", columnspan=2)

frm_bottom = tk.Frame(master=window)
frm_bottom.grid(row=3, column=0, pady=1, sticky="nsew", columnspan=2)

btn_4 = tk.Button(master=window, text="<<")
btn_4.grid(row=3, column=0, pady=1, sticky="nsew")

btn_5 = tk.Button(master=window, text=">>")
btn_5.grid(row=3, column=1, pady=1, sticky="nsew")

window.mainloop()
