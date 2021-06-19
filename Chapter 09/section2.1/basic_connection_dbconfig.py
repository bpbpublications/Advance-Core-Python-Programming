import mysql.connector as msql
import credentials as c
pycon = msql.connect(**c.dbConfig)
print(pycon)
pycon.close()
