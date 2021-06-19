import mysql.connector as msql
import credentials as c
pycon = msql.connect(**c.dbConfig)
mycursor = pycon.cursor()
mycursor.execute('SHOW DATABASES;')
result_set = mycursor.fetchall()
for result in result_set:
    print(result)
pycon.close()
print('Done!!')
