#Import tkinter
from tkinter import*
#import mysql.connector
import mysql.connector as msql
#import credentials.py which has login details
import credentials as c

#define a function to create table
def insert_val():
    pycon = msql.connect(**c.dbConfig)
    mycursor = pycon.cursor()
    statement = "INSERT INTO "+str(table_name_E.get())+"(FABRIC_NAME,IMPORT_EXPORT,COST_PER_METER,COLORS_AVAILABLE) VAlUES("+"'"+str(column1_E.get())+"',"+"'"+str(column2_E.get())+"',"+"{0},{1});".format(int(column3_E.get()),int(column4_E.get()))
    print("Passing following information to MySQL textile database:"+statement)
    mycursor.execute(statement)
    pycon.commit()
    pycon.close()
    print('Done!!') 
    
#Create instance of window
mw = Tk()
mw.geometry('400x400')
table_name = Label(mw, text = 'TABLE NAME')
table_name.place(x =10, y =10)

table_name_E = Entry(mw,bd = 2)
table_name_E.place(x = 150, y =10)

column1 = Label(mw, text = 'FABRIC_NAME')
column1.place(x = 10 , y = 60)

column1_E = Entry(mw,bd = 2)
column1_E.place(x = 150 , y = 60 )

column2 = Label(mw, text = 'IMPORT_EXPORT')
column2.place(x = 10 , y = 110)

column2_E = Entry(mw,bd = 2)
column2_E.place(x = 150 , y = 110 )

column3 = Label(mw, text = 'COST_PER_METER')
column3.place(x = 10, y = 160 )

column3_E = Entry(mw,bd = 2)
column3_E.place(x = 150, y = 160 )

column4 = Label(mw, text = 'COLORS_AVAILABLE')
column4.place(x = 10, y = 210)

column4_E = Entry(mw,bd = 2)
column4_E.place(x = 150, y = 210 )


insert_button = Button(mw,text = 'INSERT VALUES', command = insert_val)
insert_button.place(x = 40 , y = 260)

mw.mainloop()
