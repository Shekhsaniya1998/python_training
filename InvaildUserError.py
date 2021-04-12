class InvalidUserError(Exception):
    def __init__(self,message):
        self.message=message



class user:
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
    def verify(self):
        if(self.name=="abc" and
           self.uid=="12"):
            return true
        else:

             raise(InvalidUserError("Invalid user"))
u=user("abc",12)

try:
    print(u.verify())
except InvalidUserError as e:
    print(e.message)
