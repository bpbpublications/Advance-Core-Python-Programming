#import statements
from tkinter import*
import time

start_time = 0
end_time = 0
total_time = 0

def time_display(seconds):
#get the floor value of minutes by dividing value of seconds by 60
    minutes = seconds//60
#get the floor value of hours by dividing value of minutes by 60
    hours = minutes//60
    minutes = minutes%60
    seconds = seconds%60
    msg = "Time Lapsed = {0}:{1}:{2}".format(int(hours),int(minutes),int(seconds))
    lbl = Label(mw,text = msg,fg = "blue",bg = "white",font=("Comic Sans MS",14,"bold italic"),width = 100, height = 100 )
    lbl.pack(side = "top")

def timer_start():
    global start_time
    print("in start time")
    start_time = time.time()
    print(start_time)

def timer_end():
    end_time = time.time()
    total_time = end_time - start_time
    time_display(int(total_time))

#Create root window
mw = Tk()
mw.geometry("300x300")
#Create a frame Object
mf = Frame(mw)
#attach frame to root window
mf.pack(side = "bottom")

#First button
button1 = Button(mf, text = "Start",bg = "green", bd = 10,command = timer_start)

#Attach button1 to the frame on the left side
button1.pack(side = "left")

#Second Button
button2 = Button(mf, text = "Stop",bg = "red",bd = 10,command = timer_end)

#Attach button2 to the frame on the right side
button2.pack(side = "right")

#Main Loop
mw.mainloop()
