class User:
    def __init__(self,fname,did,lname):
        self.fname=fname
        self.did=did
        self.lname=lname
    def displayuser(self):
        print(self.fname,self.did,self.lname)

u=User("saniya",12,"shekh")
u.displayuser()
