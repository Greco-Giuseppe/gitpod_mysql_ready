import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="prova3"
)

mycursor = mydb.cursor()

sql = "INSERT INTO tabella (name, address) VALUES (%s , %s)"    #%s stringa  %d intero    #name address  in alto alla tabella eexit
val = ("Giuseppe" , "Milano 18")

mycursor.execute(sql, val)

mydb.commit() # apporta le modifiche

print(mycursor.rowcount , "inserito")
