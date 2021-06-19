import mysql.connector as msql
pycon = msql.connect(host = 'localhost',user='pymysqladmin',passwd='pymysql123',charset='utf8',database='pymysql')
mycursor = pycon.cursor()
statement = """UPDATE BOOK_LIBRARY SET BOOK_ID = 2 WHERE BOOK_ID = 12;"""
mycursor.execute(statement)
pycon.commit()
pycon.close()
print("Done!!")
