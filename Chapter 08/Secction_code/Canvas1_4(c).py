#Import tkinter
from tkinter import*

#Create instance of window
mw = Tk()

#Create instance of Canvas class
mc = Canvas(mw, width = 200, height = 200)

#create lines to join point 2, 3 and 4 together
line = mc.create_line(200,0,0,200,200,200,200,0,fill = "orange")

#Pack canvas object mc on to window object mw
mc.pack()

#Call mainloop()
mw.mainloop()
