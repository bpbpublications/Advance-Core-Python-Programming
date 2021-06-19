#Import tkinter
from tkinter import*

#Create instance of window
mw = Tk()

#Create instance of Canvas class
mc = Canvas(mw, width = 200, height = 200)


#create an Arc
arc = mc.create_arc(50,25,150,100,start=0, extent = 359,width = 4, fill = "green", outline = "Purple", activefill = "White")

#Pack canvas object mc on to window object mw
mc.pack()

#Call mainloop()
mw.mainloop()
