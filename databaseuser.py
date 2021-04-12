import mysql.connector
# code for user log 
class user:
       
         def __init__(self,uid):
       # self.uname=uname
             self.uid=uid
         def user_log(self):


             mydb=mysql.connector.connect(
             host="localhost",
             user="root",
             password="root",
             database="python"
             )
        
             mycursor=mydb.cursor()
             mycursor.execute("SELECT user_id FROM userlog")
             my_result=[]
             my_result=mycursor.fetchone()


  
             #mycursor.execute("SELECT user_name FROM userlog")
             #my_result1=[]
            # my_result1=mycursor.fetchall()

             for user_id in my_result:
                 
                 if(self.uid==user_id):
                    print("Welcome" + " " + "Sucessfully logged in")
                    break
                

       # else:
           # print("Invalid user")
uid=int(input("Enter the user_id  "))
#uname=(input("Enter the user name:"))
u=user(uid)
u.user_log()
