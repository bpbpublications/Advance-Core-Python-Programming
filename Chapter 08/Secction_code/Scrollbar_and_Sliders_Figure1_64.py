import tkinter as tk

#content for textbox
list_of_month = "January\nFebruary\nMarch\nApril\nMay\nJune\nJul\nAugust\nSeptember\nOctober\nNovember\nDecember\n"
list_of_days = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday"

mw = tk.Tk()
mw.geometry("100x100")

#Vertical Scrollbar
sb = tk.Scrollbar(mw)
sb.pack(side = tk.RIGHT,fill="y")

#Horizontal Scroll bar
sb2 = tk.Scrollbar(mw,orient = tk.HORIZONTAL)
sb2.pack(side = tk.BOTTOM, fill="x")

#Create a Textbox
tb = tk.Text(mw,height = 500, width = 500, yscrollcommand = sb.set,xscrollcommand = sb2.set, wrap = "none", bg="sky blue")
tb.pack()

sb.config(command = tb.yview)
sb2.config(command = tb.xview)

tb.insert(tk.END,list_of_month)
tb.insert(tk.END,list_of_days)

mw.mainloop()
