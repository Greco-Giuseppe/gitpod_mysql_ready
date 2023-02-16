#riempire una tabella 
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="" ,
  database = 'prova'
) 

mycursor = mydb.cursor()

sql = "INSERT INTO customers2 (name, address) VALUES (%s, %s)"  #insert into   #RECORD?
val = ("Giuseppe", "Bicocca")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")