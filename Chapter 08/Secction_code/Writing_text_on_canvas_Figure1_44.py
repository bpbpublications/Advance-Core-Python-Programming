#Import tkinter
from tkinter import*

#Create instance of window
mw = Tk()

#Create instance of Canvas class
mc = Canvas(mw,bg="pink",width = 400, height = 400 )

#Define Font for text on canvas
fnt = ('Times',15,"bold")

#Define the text
txt = mc.create_text(150,50, text = "Black and White", font = fnt,fill ="black",activefill = "white")

#Add canvas object mc on to window object mw
mc.pack()

#Call mainloop()
mw.mainloop()

