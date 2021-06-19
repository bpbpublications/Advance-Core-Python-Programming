import mysql.connector as msql
pycon = msql.connect(host = 'localhost',user='pymysqladmin',passwd='pymysql123',charset='utf8',database='pymysql')
mycursor = pycon.cursor()
statement = """SELECT * FROM BOOK_LIBRARY;"""
mycursor.execute(statement)
result_set = mycursor.fetchall()
print("The Results are as follows: ")
for result in result_set:
    print(result)
pycon.close()
print("Done!!")
