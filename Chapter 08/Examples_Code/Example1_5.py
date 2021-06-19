#Example 14.5
#Write a code that click of the button we want to display a message box with a message “Welcome to the world of Widgets”
#import Statements
from tkinter import*
import tkinter.messagebox

# Create a function for button
def message_display():
    tkinter.messagebox.showinfo("Welcome Note","welcome to the world of Widgets")

#Create instance of window
mw = Tk()

#set the size of the window
mw.geometry("150x150")


#Create instance of a button. 
my_first_button = Button(mw, text="Click Here", command = message_display)

#For the button to display pack the button on to the window
my_first_button.pack()

#call the mainloop()
mw.mainloop()

