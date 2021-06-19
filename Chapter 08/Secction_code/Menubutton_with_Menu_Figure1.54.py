#Import statements
from tkinter import*

#Create root window(+120 +120 is the distance from xy)
mw = Tk()
mw.geometry("300x300+100+100")

#Create Menu Button
mb = Menubutton(mw,text = "File")
mb.grid()

#Create a pull down menu
mb.menu = Menu(mb,tearoff=0)
mb["menu"] = mb.menu

# Add commands to pull down menu
mb.menu.add_command(label = "New File")
mb.menu.add_command(label = "Open")
mb.menu.add_command(label = "Recent Files")
mb.menu.add_command(label = "Save")
mb.menu.add_command(label = "Save As")
mb.menu.add_command(label = "Print")
mb.menu.add_command(label = "Close")
mb.menu.add_command(label = "Exit")

#Call Main Loop Method
mw.mainloop()
