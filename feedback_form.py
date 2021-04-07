class feedback_form:
    def __init__(self,PID,PNAME,RATINGS,DESCRIPTION):
        self.PID=PID
        self.PNAME=PNAME
        self.RATINGS=RATINGS
        self.DESCRIPTION=DESCRIPTION
    def display_feedback(self):
        print("Patient id:",self.PID,'\n',
              "Patient name:",self.PNAME,'\n',
              "Ratings :",self.RATINGS,'\n',
              "Description :",self.DESCRIPTION)
f=feedback_form("12","ABC","*****","NOTHING")
f.display_feedback()
