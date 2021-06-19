#Example 14.9
#Import tkinter
from tkinter import*

#Create instance of window
mw = Tk()

#Create instance of Canvas class
mc = Canvas(mw, width = 200, height = 200)

#create rectangle
rect = mc.create_rectangle(5,10,100,50,fill = "Purple", width = 10)

#Pack canvas object mc on to window object mw
mc.pack()

#Call mainloop()
mw.mainloop()

