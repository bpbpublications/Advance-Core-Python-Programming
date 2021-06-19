#Import tkinter
from tkinter import*

#Create instance of window
mw = Tk()

#Create instance of Canvas class
mc = Canvas(mw, width = 200, height = 200)

#create line
line = mc.create_line(200,0,0,200,fill = "Purple", width = 10)
line2 = mc.create_line(0,0,200,200,fill = "Blue", width = 10)

#Pack canvas object mc on to window object mw
mc.pack()

#Call mainloop()
mw.mainloop()
