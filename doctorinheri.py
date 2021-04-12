from userinher import *
class Doctor(User):
    def __init__(self,fname,uid,lname,did):
        super().__init__(fname,did,lname)
        self.did=did
        #self.uid=uid
    def displaydoctor(self):
        print(self.fname,self.did,self.lname)
d=Doctor("xyz",32,"lmn",45)
d.displaydoctor()
u=User("abc",10,"def")
print("from doctor file changining values ",u.displayuser())

