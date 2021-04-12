import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    #database="python"
    )

mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE PYTHON")
#mycursor.execute("USE PYTHON")
mycursor.execute("CREATE TABLE CUSTOMERS(NAME VARCHAR(200),ADDRESS VARCHAR(100),PHONE_NO INT(50))")
sql="INSERT INTO CUSTOMERS(NAME,ADDRESS,PHONE_NO) VALUES(%s,%s)"
val=("abc","bnglr",123456789)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")
