import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="49154",
  user="retail_user",
  password="root"
)

print(mydb)