import mysql.connector

myconnection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password"
)

print(myconnection)

db_name="python_test_db"
sqlquery="CREATE DATABASE " + db_name

mycursor=myconnection.cursor()

mycursor.execute(sqlquery)
print("Create Database successfully")