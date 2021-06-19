from tkinter import*
mw = Tk()
mw.geometry("150x150")
img = PhotoImage(file = "f:\\my_images\\sky.gif")

#Vertical Scrollbar
sb = Scrollbar(mw)
sb.pack(side = RIGHT,fill="y")

#Horizontal Scroll bar
sb2 = Scrollbar(mw,orient = HORIZONTAL)
sb2.pack(side = BOTTOM, fill="x")

#Create text
ta = Text(mw,yscrollcommand = sb.set,xscrollcommand = sb2.set)

#Configure scrollbars to text widget
sb.config(command = ta.yview)
sb2.config(command = ta.xview)

#insert content
ta.insert(INSERT,"Sky is the limit!!")
ta.image_create(END,image=img)

ta.pack()
mw.mainloop()
