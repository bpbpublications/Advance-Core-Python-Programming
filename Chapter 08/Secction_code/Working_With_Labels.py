#Import Statements
from tkinter import*

#Create a root window
mw = Tk()

#Define dimensions of root window
mw.geometry("200x200")

#Create Label and define options such as font, width, height, bg,fg etc
lbl = Label(mw,text="I am your first label",fg = "blue",bg = "green",font=("Comic Sans MS",14,"bold italic"),width = 200, height = 200 )

#Associate the label to the root window
lbl.pack()

#Call the mainloop()
mw.mainloop()
