#import statements
from tkinter import*

mw = Tk()
mw.geometry("200x200")

#Create a frame Object
mf = Frame(mw,width =150, height = 150,bg= "green",bd = 20, relief = "sunken")

#attach frame to root window
mf.pack()

#Main Loop
mw.mainloop()

