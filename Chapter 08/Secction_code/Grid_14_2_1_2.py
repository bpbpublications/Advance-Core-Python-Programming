import tkinter as tk

mw = tk.Tk() 

labelusern = tk.Label(mw, text = "User Name")
labelusern.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)

labelpwd  = tk.Label(mw,text = "Password")
labelpwd.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.S)


entryusern = tk.Entry(mw, width=20)
entrypwd = tk.Entry(mw, width=20)

entryusern.grid(column=1, row=0, padx=10, pady=5, sticky=tk.N)
entrypwd.grid(column=1, row=1, padx=10, pady=5, sticky=tk.S)


loginButton = tk.Button(mw, text = 'Login')
loginButton.grid(column=0, row=2, pady=10, sticky=tk.W)


mw.mainloop()
