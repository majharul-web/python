import mysql.connector

db_name="python_test_db"
myconnection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database=db_name
)

print(myconnection)

mycursor=myconnection.cursor()

sqlquery="""
         CREATE TABLE Student
         (
             Roll varchar(4),
             Name varchar(50)
         )
        """
mycursor.execute(sqlquery)
print("Create Table successfully")