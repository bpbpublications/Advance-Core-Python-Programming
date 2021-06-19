#Import tkinter
from tkinter import*
from tkinter import messagebox
#import mysql.connector
import mysql.connector as msql
#import credentials.py which has login details
import credentials as c


def display_result():
    print("var = ",var.get())
    pycon = msql.connect(**c.dbConfig)
    mycursor = pycon.cursor()
    statement = ""
    
    if (var.get() == 1):
          statement = "SELECT * FROM FABRIC;"
    elif (var.get() == 2):
        
        statement+= "SELECT "
        
        if(svar1.get() == 1):
            statement+= "FABRIC_ID "
            
        if(svar1.get() == 1 and svar2.get() == 1):
            statement+= ", FABRIC_NAME "
        elif(svar1.get() == 0 and svar2.get() == 1):
            statement+= "FABRIC_NAME "
        
        if((svar1.get() == 1 or svar2.get() == 1) and svar3.get() == 1):
            statement+= ", IMPORT_EXPORT "
        elif((svar1.get() == 0 and svar2.get() == 0) and svar3.get() == 1):
            statement+= "IMPORT_EXPORT "
        
        if((svar1.get() == 1 or svar2.get() == 1 or svar3.get() == 1) and svar4.get() == 1):
            statement+= ", COST_PER_METER "
        elif((svar1.get() == 0 and svar2.get() == 0 and svar3.get() == 0) and svar4.get() == 1):
            statement+= "COST_PER_METER "
            
        if((svar1.get() == 1 or svar2.get() == 1 or svar3.get() == 1 or svar4.get() == 1)and svar5.get() == 1):
            statement+= " , COLORS_AVAILABLE "
        elif((svar1.get() == 0 and svar2.get() == 0 and svar3.get() == 0 and svar4.get() == 0)and svar5.get() == 1):
            statement+= " COLORS_AVAILABLE "
        
        statement+= "FROM FABRIC WHERE "
        if(cvar1.get() == 1):
            statement+= "FABRIC_ID = '{}' ".format(str(fabricIdCheck2entry.get()))
            
        if(cvar1.get() == 1 and cvar2.get() == 1):
            statement+= " AND FABRIC_NAME = '{}' ".format(str(fabricNameCheck2entry.get()))
            
        elif(cvar1.get() == 0 and cvar2.get() == 1):
            statement+= " FABRIC_NAME = '{}' ".format(str(fabricNameCheck2entry.get()))
            
        if((cvar1.get() == 0 and cvar2.get() == 0) and cvar3.get() == 1):
            statement+= " IMPORT_EXPORT = '{}' ".format(str(ieCheck2entry.get()))
            
            
        elif((cvar1.get() == 1 or cvar2.get() == 1) and cvar3.get() == 1):
            statement+= " AND IMPORT_EXPORT = '{}' ".format(str(ieCheck2entry.get()))
        
            
        if((cvar1.get() == 0 and cvar2.get() == 0 and cvar3.get() == 0) and cvar4.get() == 1):
            statement+= " COST_PER_METER = {} ".format(int(costCheck2entry.get()))

        elif((cvar1.get() == 1 or cvar2.get() == 1 or cvar3.get() == 1) and cvar4.get() == 1):
            statement+= " AND COST_PER_METER = {} ".format(int(costCheck2entry.get()))

        if((cvar1.get() == 0 and cvar2.get() == 0 and cvar3.get() == 0 and cvar4.get() == 0)and cvar5.get() == 1):
            statement+= " COST_PER_METER = {} ".format(int(colorsCheck2entry.get()))
        elif((cvar1.get() == 1 or cvar2.get() == 1 or cvar3.get() == 1 or cvar4.get() == 1)and cvar5.get() == 1):
            statement+= " AND COST_PER_METER = {} ".format(int(colorsCheck2entry.get()))
            
    statement += ";"
    mycursor.execute(statement)
    result_set = mycursor.fetchall()
    for result in result_set:
        print(result)
    messagebox.showinfo("FABRIC from TEXTILE",result_set)
    pycon.close()
    print('Done!!') 
    
#Create instance of window
mw = Tk()
mw.geometry('600x600')
#Variable for Radio
var = IntVar()
#Variable for Checkbutton
cvar1 = IntVar()
cvar2 = IntVar()
cvar3 = IntVar()
cvar4 = IntVar()
cvar5 = IntVar()

svar1 = IntVar()
svar2 = IntVar()
svar3 = IntVar()
svar4 = IntVar()
svar5 = IntVar()
#Radio button SELECT ALL
selectRadio = Radiobutton(mw, text = 'SELECT ALL',variable=var, value=1)
selectRadio.place(x =10, y =10)

#SELECT FILTER
selectFilterRadio = Radiobutton(mw, text = 'SELECT WHERE',variable=var, value=2)
selectFilterRadio.place(x = 10, y =60)

#LABEL SELECT

selectLabel = Label(mw, text = 'SELECT',font='Bold')
selectLabel.place(x = 10 , y = 110)

#CHECKS FOR SELECT

#FABRIC ID

fabricIdCheck = Checkbutton(mw,text='FABRIC_ID',variable = svar1, onvalue = 1,offvalue = 0)
fabricIdCheck.place(x = 10 , y = 170 )

#FABRIC NAME

fabricNameCheck = Checkbutton(mw,text='FABRIC_NAME',variable = svar2, onvalue = 1,offvalue = 0)
fabricNameCheck.place(x = 10 , y = 230 )

#IMPORT_EXPORT

ieCheck = Checkbutton(mw,text='IMPORT_EXPORT',variable = svar3, onvalue = 1,offvalue = 0)
ieCheck.place(x = 10 , y = 290 )

#COST

costCheck = Checkbutton(mw,text='COST',variable = svar4, onvalue = 1,offvalue = 0)
costCheck.place(x = 10 , y = 350 )

#COLORS

colorsCheck = Checkbutton(mw, text = 'COLORS',variable = svar5, onvalue = 1,offvalue = 0)
colorsCheck.place(x = 10, y = 410 )


#LABEL WHERE

whereLabel = Label(mw, text = 'WHERE', font='Bold')
whereLabel.place(x = 180 , y = 110)


#CHECKS FOR WHERE
#FABRIC ID

fabricIdCheck2 = Checkbutton(mw,text='FABRIC_ID  = ',variable = cvar1, onvalue = 1,offvalue = 0)
fabricIdCheck2.place(x = 180 , y = 170 )
fabricIdCheck2entry = Entry(mw, bd = 2)
fabricIdCheck2entry.place(x = 310, y = 170)

#FABRIC NAME

fabricNameCheck2 = Checkbutton(mw,text='FABRIC_NAME  = ',variable = cvar2, onvalue = 1,offvalue = 0)
fabricNameCheck2.place(x = 180 , y = 230 )
fabricNameCheck2entry = Entry(mw, bd = 2)
fabricNameCheck2entry.place(x = 310, y = 230)


#IMPORT_EXPORT

ieCheck2 = Checkbutton(mw,text='IMPORT_EXPORT  = ',variable = cvar3, onvalue = 1,offvalue = 0)
ieCheck2.place(x = 180 , y = 290 )
ieCheck2entry = Entry(mw, bd = 2)
ieCheck2entry.place(x = 310, y = 290)

#COST

costCheck2 = Checkbutton(mw,text='COST  = ',variable = cvar4, onvalue = 1,offvalue = 0)
costCheck2.place(x = 180 , y = 350 )
costCheck2entry = Entry(mw, bd = 2)
costCheck2entry.place(x = 310, y = 350)

#COLORS

colorsCheck2 = Checkbutton(mw, text = 'COLORS  = ',variable = cvar5, onvalue = 1,offvalue = 0)
colorsCheck2.place(x = 180, y = 410 )
colorsCheck2entry = Entry(mw, bd = 2)
colorsCheck2entry.place(x = 310, y = 410)

#DISPLAY RESULTS
display_button = Button(mw,text = 'DISPLAY RESULT',command = display_result)
display_button.place(x = 180 , y = 470)


mw.mainloop()
