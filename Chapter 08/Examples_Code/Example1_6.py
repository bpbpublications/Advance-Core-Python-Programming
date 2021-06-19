#Example 14.6
#Write a program for two buttons one on the left and the other on the right. Try it out and match your results with the output given in the book.

#import Statements
from tkinter import*
import tkinter.messagebox


# Create a function for right button
def message_display_right():
    tkinter.messagebox.showinfo("Next Topic","Welcome to Canvas")

# Create a function for right button
def message_display_left():
    tkinter.messagebox.showinfo("Previous Topic","Welcome to Widgets")

#Create instance of window
mw = Tk()
mw.title("Select Topic")
#Create instance of a button

my_first_button = Button(mw,text="Next",fg="Green", command = message_display_right)
my_second_button = Button(mw,text="Previous",fg="Red", command = message_display_left)

#Adjust the position of buttons
my_first_button.pack(side = tkinter.RIGHT)
my_second_button.pack(side = tkinter.LEFT)

#call the mainloop()
mw.mainloop()

