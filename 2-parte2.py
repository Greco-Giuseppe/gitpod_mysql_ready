#Per creare una tabella in MySQL   # istruzione "CREATE TABLE".

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="prova3"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")    

#If this page is executed with no error, you have successfully created a table named "customers".

#Puoi controllare se esiste una tabella elencando tutte le tabelle nel tuo database # istruzione "SHOW TABLES":   # mycursor.execute("SHOW TABLES")

# CHIAVE PRIMARIA
#Quando crei una tabella, dovresti anche creare una colonna con una chiave univoca
#'istruzione "INT AUTO_INCREMENT PRIMARY KEY" che inserirà un numero univoco per ogni record. A partire da 1 e aumentato di uno per ogni record.
#record = righe

#Crea chiave primaria durante la creazione della tabella:


mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#Se la tabella esiste già, utilizzare la parola chiave ALTER TABLE:

#Crea chiave primaria su una tabella esistente:


mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



# fetchall ultimo comando da imparare 