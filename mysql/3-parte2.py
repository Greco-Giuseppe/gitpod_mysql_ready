#INSERIRE NELLA TABELLA

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",    # localhost -> la mia stessa macchina
  user="root",       # i nomi vanno modificati in base a quelli dell'utente (GUARDARE IN MAIN.PY) -->   host="localhost",   user="root",  password=""
  password="" ,
  database="prova3"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s , %s)"    #%s stringa  %d intero 
val = ("Giuseppe" , "Milano 18")

mycursor.execute(sql, val)

mydb.commit() # apporta le modifiche

print(mycursor.rowcount , "inserito")