#import Statements
from tkinter import*

# Create a function for button
def arc_display():

#Create instance of Canvas class
    mc = Canvas(mw, width = 350, height = 350)

#Take inputs for all values    
    x0 = int(input("please enter the value for  x0 : "))
    y0 = int(input("please enter the value for  y0 : "))

    x1 = int(input("please enter the value for  x1 : "))
    y1 = int(input("please enter the value for  y1 : "))

    s_angle = int(input("please enter the value for  start angle : "))
    e_angle = int(input("please enter the value for  extent angle : "))

#Create an arc with the given value
    mc.create_arc(x0,y0,x1,y1,start = s_angle,extent = e_angle)

#Make Canvas visible on the root window    
    mc.pack()

#Create instance of window
mw = Tk()

#Create instance of a button. 
my_first_button = Button(mw, text="Create Arc", command = arc_display)

#For the button to display pack the button on to the window
my_first_button.pack()

#call the mainloop()
mw.mainloop()
