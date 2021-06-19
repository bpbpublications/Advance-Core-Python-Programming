#Import tkinter
from tkinter import*

#Create instance of window
mw = Tk()

#Create instance of Canvas class
mc = Canvas(mw, width = 200, height = 200)

#Create outline of rectangle
rect = mc.create_rectangle(50,25,150,100,outline = "Red")

#create an Arc
arc = mc.create_arc(50,25,150,100, start = 120, extent = 90)

#Pack canvas object mc on to window object mw
mc.pack()

#Call mainloop()
mw.mainloop()
