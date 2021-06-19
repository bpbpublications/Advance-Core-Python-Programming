import mysql.connector as msql
pycon = msql.connect(host = 'localhost',user='root',passwd='bpb12',charset='utf8')
mycursor = pycon.cursor()
statement = 'CREATE database SCHOOL;'
mycursor.execute(statement)
mycursor.execute("SHOW DATABASES;")
mycursor.fetchall()
mycursor.close()

###########################################333
#drop the database
statement = 'DROP DATABASE SCHOOL;'
mycursor.execute(statement)
mycursor.execute("SHOW DATABASES;")
mycursor.fetchall()
mycursor.close()
#################################################
import mysql.connector as msql
pycon = msql.connect(host = 'localhost',user='pymysqladmin',passwd='pymysql123',charset='utf8',database='pymysql')
mycursor = pycon.cursor()
statement = """CREATE TABLE BOOK_LIBRARY(BOOK_ID SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT, BOOK_NAME CHAR(20) NOT NULL,AUTHOR_NAME CHAR(20) NOT NULL, PAGES SMALLINT NOT NULL,COST SMALLINT NOT NULL )"""
mycursor.execute(statement)
statement = 'SHOW COLUMNS FROM BOOK_LIBRARY;'
mycursor.execute(statement)
mycursor.fetchall()
pycon.close()
