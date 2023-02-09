

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",    # localhost -> la mia stessa macchina
  user="root",       # i nomi vanno modificati in base a quelli dell'utente (GUARDARE IN MAIN.PY) -->   host="localhost",   user="root",  password=""
  password="" ,
   #database="mydatabase"    # per connettersi al database "mydatabase"   (per provare ad accedere al database quando effettui la connessione)
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE prova") #Per creare un database in MySQL, usa l'istruzione "CREATE DATABASE":

mycursor.execute("SHOW DATABASES") #Puoi controllare se esiste un database elencando tutti i database nel tuo sistema usando l'istruzione "SHOW DATABASES":
 #python non puo mostrare i databese 





