class user:
   # user_id=123
    #user_name="saniya"
   # password="abc"
    uid=" "
    pasw=" "
    def __init__(self,ufname,ulname,DOB,
                 street,city,state,country,pin):
        self.ufname=ufname
        self.ulname=ulname
        #self.uid=user_id
        self.DOB=DOB
        self.street=street
        self.city=city
        self.state=state
        self.country=country
        self.pin=pin
    def displayuser(self):
        print("first Name :",self.ufname,"Last Name :",self.ulname,
               "Date of birth : ",self.DOB,
              "Street : ",self.street,"City : ",self.city,
              "Country : ",self.country,"Pin : ",self.pin)
    def Verifyuser(self,userid,password):
        if(user.uid== userid
           and user.pasw== password):
            print("User verification Done. Welcome To Hospital")
        else:
            print("Invalid user_id or Password")
u=user("saniya","shekh","14- 03 -1998","Karnataka",
       "sada shiva nagar","Tumukur",
       "India","572102")
u.displayuser()
userid=int(input("Enter the user id:"))
password=input("Enter the password:")
u.Verifyuser(userid,password)
#print(__doc__)
#print(__dict__)
print(__name__)
print(__file__)
       
            
        
        
