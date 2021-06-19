import mysql.connector as msql
data =[]
pycon = msql.connect(host = 'localhost',user='pymysqladmin',passwd='pymysql123',charset='utf8',database='pymysql')
mycursor = pycon.cursor()
statement = """INSERT INTO BOOK_LIBRARY(BOOK_NAME,AUTHOR_NAME,PAGES,COST) VALUES (%s,%s,%s,%s);"""
#Get Name of the Book
val1 = input("Enter Book Name : ")

#Append value to list
data.append(val1)

#Get Name of the Author
val2 = input("Enter Author Name : ")

#Append value to list
data.append(val2)

#Get value of number of pages and convert to int
val3 = int(input("Enter Number of Pages: "))

#Append value to list
data.append(val3)

#Get value of cost and convert to int
val4 = int(input("Enter Cost in $: "))

#Append value to list
data.append(val4)

#Convert list to tuple
data2 = tuple(data)

print(data2)
mycursor.execute(statement,data2)
pycon.commit()
pycon.close()
