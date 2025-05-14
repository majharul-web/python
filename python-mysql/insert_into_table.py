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
         INSERT INTO Student
         (Roll,Name)
         VALUES ('101','Masud rana')
        """
mycursor.execute(sqlquery)
myconnection.commit()
print("Insert data successfully")