import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()    # stessa cosa di scrivere sul terminale ma lo faccio fare a lui

mycursor.execute("CREATE DATABASE mydatabase")

