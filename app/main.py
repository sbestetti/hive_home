import tkinter as tk

window = tk.Tk()
window.minsize(240, 320)

btn_1 = tk.Button(master=window, text="Quarto")
btn_1.grid(row=0, column=0, pady=3)

btn_2 = tk.Button(master=window, text="Banheiro")
btn_2.grid(row=1, column=0, pady=3)

btn_3 = tk.Button(master=window, text="Corredor")
btn_3.grid(row=2, column=0, pady=3)

btn_4 = tk.Button(master=window, text="<<")
btn_4.grid(row=4, column=0, pady=3)

btn_5 = tk.Button(master=window, text=">>")
btn_5.grid(row=4, column=1, pady=3)

window.mainloop()
