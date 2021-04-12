import   mysql.connector
 
def verifyuser(userid, user_id):
    mydb =  mysql.connector.connect(host="localhost",

                user="root",password="root", database="python")
    mycursor = mydb.cursor()
    sql = "select user_name from userlog where user_id = %s"
    val = [userid]
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    if (result != None):
        if(user_name == result[0]):
            return True
        else:
            return False
    else:
        return False
 
print(verifyuser("smith",1))
