import tkinter as tk

window = tk.Tk()
window.minsize(240, 320)

frm_main = tk.Frame(
    master=window,
    borderwidth=1,
    relief=tk.RAISED
)
frm_main.grid(row=0, column=0, pady=3)
btn_1 = tk.Button(master=frm_main, text="Quarto")
btn_1.pack()

frm_main = tk.Frame(
    master=window,
    borderwidth=1,
    relief=tk.RAISED
)
frm_main.grid(row=1, column=0, pady=3)
btn_2 = tk.Button(master=frm_main, text="Banheiro")
btn_2.pack()

frm_main = tk.Frame(
    master=window,
    borderwidth=1,
    relief=tk.RAISED
)
frm_main.grid(row=2, column=0, pady=3)
btn_3 = tk.Button(master=frm_main, text="Corredor")
btn_3.pack()

frm_main = tk.Frame(
    master=window,
    borderwidth=1,
    relief=tk.RAISED
)
frm_main.grid(row=4, column=0, pady=3)
btn_4 = tk.Button(master=frm_main, text="<<")
btn_4.pack()

frm_main = tk.Frame(
    master=window,
    borderwidth=1,
    relief=tk.RAISED
)
frm_main.grid(row=4, column=1, pady=3)
btn_5 = tk.Button(master=frm_main, text=">>")
btn_5.pack()

window.mainloop()
