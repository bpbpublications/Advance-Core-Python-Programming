import mysql.connector as msql
pycon = msql.connect(host = 'localhost',user='pymysqladmin',passwd='pymysql123',charset='utf8',database='pymysql')
mycursor = pycon.cursor()
statement = """INSERT INTO BOOK_LIBRARY(BOOK_NAME,AUTHOR_NAME,PAGES,COST) VALUES ('{0}','{1}',{2},{3});"""
val1 = input("Enter Book Name : ")
val2 = input("Enter Author Name : ")
val3 = int(input("Enter Number of Pages: "))
val4 = int(input("Enter Cost in $: "))
mycursor.execute(statement.format(val1,val2,val3,val4))
pycon.commit()
pycon.close()



