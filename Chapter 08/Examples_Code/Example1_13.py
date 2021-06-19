#import Statements
from tkinter import*

#Create instance of window
mw = Tk()

#Create instance of Canvas class
mc = Canvas(mw, width = 350, height = 350)

#Draw an  oval
mc.create_oval(20,20,200,200,fill = "yellow")

#Make Canvas visible on the root window    
mc.pack()

#call the mainloop()
mw.mainloop()
