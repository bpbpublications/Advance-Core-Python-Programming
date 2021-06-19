#Example 14.4: 
#Write a program to change the image of the root window.

#import tkinter
from tkinter import*

#create root window
mw = Tk()

#Set the title for your root window
mw.title("my First window")

#Set the size of the window
mw.geometry("600x400")

#set the image icon for the window (For this example the image is at F:/my_images/drop.ico)
mw.wm_iconbitmap("F:/my_images/drop.ico")

mw.mainloop()
