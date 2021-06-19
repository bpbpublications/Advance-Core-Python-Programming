#import Statements
from tkinter import*

#Create instance of window
mw = Tk()

#Create instance of Canvas class
mc = Canvas(mw, width = 350, height = 350)

#Draw Polygon
mc.create_arc(30,65,300,250,start = 0, extent = 270, fill="yellow",width = 5,outline="black")

#plot all points for inner dressing of pizza
mc.create_oval(80,120,94,134,fill="red",outline = "black")
mc.create_oval(210,80,224,94,fill="red",outline = "black")
mc.create_oval(110,130,124,144,fill="red",outline = "black")
mc.create_oval(200,110,214,124,fill="red",outline = "black")
mc.create_oval(150,70,164,84,fill="red",outline = "black")
mc.create_oval(150,100,164,114,fill="red",outline = "black")
mc.create_oval(130,200,144,214,fill="red",outline = "black")
mc.create_oval(100,200,114,214,fill="red",outline = "black")
#Make Canvas visible on the root window    
mc.pack()

#call the mainloop()
mw.mainloop()
