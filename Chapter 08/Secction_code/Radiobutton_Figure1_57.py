#Import statements
from tkinter import*

#Create root window
mw = Tk()
mw.geometry("300x300")

#Create Radio Button
rb1 = Radiobutton(mw,text = "C")
rb2 = Radiobutton(mw,text = "C++")
rb3 = Radiobutton(mw,text = "Java")
rb4 = Radiobutton(mw,text = "Python")
rb5 = Radiobutton(mw,text = "Perl")

rb1.grid(row = 0,column = 0,sticky=W)
rb2.grid(row = 1,column = 0,sticky=W)
rb3.grid(row = 2,column = 0,sticky=W)
rb4.grid(row = 3,column = 0,sticky=W)
rb5.grid(row = 4,column = 0,sticky=W)

#Call Main Loop Method
mw.mainloop()
