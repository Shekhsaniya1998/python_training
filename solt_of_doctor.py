class solt_of_doctor:
    def __init__(self,DID,PID,DATE,TIME,STATUS):
        self.DID=DID
        self.PID=PID
        self.DATE=DATE
        self.TIME=TIME
        self.STATUS=STATUS
    def display_conformation(self):
        print("Doctor id:",self.DID,'\n',
              "Patient id:",self.PID,'\n',
              "Date :",self.DATE,'\n',
              "Time ",self.TIME,'\n',
              "Appointment is confirmed:",self.STATUS)

s=solt_of_doctor("30","10","08-April-2021","10:30 AM","CONFIRMED")
s.display_conformation()
