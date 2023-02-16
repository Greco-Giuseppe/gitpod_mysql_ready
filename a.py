import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="" ,
  database = 'prova'
) 

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("show tables")

for x in mycursor :
  print(x)

