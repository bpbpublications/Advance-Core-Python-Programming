#import statements
from tkinter import*
mw = Tk()

#Create a frame Object
mf = Frame(mw)
#attach frame to root window
mf.pack()

#First button
button1 = Button(mf, text = "Left",bg = "red", bd = 10)

#Attach button1 to the frame on the left side
button1.pack(side = "left")

#Second Button
button2 = Button(mf, text = "Right",bg = "Green",bd = 10)

#Attach button2 to the frame on the right side
button2.pack(side = "right")

#Main Loop
mw.mainloop()

