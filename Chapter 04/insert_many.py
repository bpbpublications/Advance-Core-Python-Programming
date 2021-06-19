import mysql.connector as msql
pycon = msql.connect(host = 'localhost',user='pymysqladmin',passwd='pymysql123',charset='utf8',database='pymysql')
mycursor = pycon.cursor()
statement = """INSERT INTO BOOK_LIBRARY(BOOK_NAME,AUTHOR_NAME,PAGES,COST) VALUES (%s,%s,%s,%s);"""
values =[('I AM Magic','Maria Robins',63,13), ('One Truth, One Law','Erin Werley',87,6), ('Mind Magic','Merlin Starlight',265,19), ('Advanced Manifesting','Linda West',172,4), ('The Frequency','Linda West',180,4)]
mycursor.executemany(statement,values)
pycon.commit()
pycon.close()
print("Records Inserted!!")
