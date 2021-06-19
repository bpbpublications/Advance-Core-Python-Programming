#import Statements
from tkinter import*
import tkinter.messagebox
from tkinter import ttk

# Create a function for right button
def message_display():
    tkinter.messagebox.showinfo("Experimenting with GIFs","Welcome to GIFs")

#Create instance of window
mw = Tk()
mw.title("Thumbs UP")

#Create instance of a button
my_first_button = ttk.Button(mw,text="click", command = message_display)
my_first_button.pack()

#Add image to button
img = PhotoImage(file = "f:\\my_images\\thumb2.gif")
my_first_button.config(image = img,compound =RIGHT)

#call the mainloop()
mw.mainloop()
