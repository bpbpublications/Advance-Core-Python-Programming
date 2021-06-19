#import Statements
from tkinter import*

#Create instance of window
mw = Tk()

#Create instance of Canvas class
mc = Canvas(mw, width = 350, height = 350)

#Draw Polygon
mc.create_polygon(250,30,200,50,230,90,60,300,100,20, fill = "pink")

#Make Canvas visible on the root window    
mc.pack()

#call the mainloop()
mw.mainloop()

