import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword",
  database="prova3"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE tabella (name VARCHAR(255), address VARCHAR(255))")
