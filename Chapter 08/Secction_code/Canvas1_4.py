#Import tkinter
from tkinter import*

#Create instance of window
mw = Tk()

#Create instance of Canvas class
mc = Canvas(mw, width = 200, height = 200)

#Add canvas object mc on to window object mw
mc.pack()

#Call mainloop()
mw.mainloop()
