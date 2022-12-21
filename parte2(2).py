#Per creare una tabella in MySQL   # istruzione "CREATE TABLE".

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")    

#If this page is executed with no error, you have successfully created a table named "customers".

#Puoi controllare se esiste una tabella elencando tutte le tabelle nel tuo database # istruzione "SHOW TABLES":   # mycursor.execute("SHOW TABLES")