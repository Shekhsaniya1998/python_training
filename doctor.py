class doctor:
    def __init__(self,DID,DNAME,DQUALIFICATION,DDOB,DSPECIALIST):
        self.DID=DID
        self.DNAME=DNAME
        self.DQUALIFICATION=DQUALIFICATION
        self.DDOB=DDOB
        self.DSPECIALIST=DSPECIALIST
    def display_doctor(self):
        print("Doctor ID:",self.DID,'\n',
              "Doctor name:",self.DNAME,'\n',
              "Doctor Qualification:",self.DQUALIFICATION,'\n',
              "Doctor Specialist:",self.DSPECIALIST,'\n')
d=doctor("30","PQRS","MBBS,MD","20-01-1990","PHYSICIAN")
d.display_doctor()

# from different file 
class prescription:
    def __init__(self,medicinces,userid,fname,did):
        self.medicinces=medicinces
        self.userid=userid
        self.fname=fname
        self.did=did
    def display_pres(self):
        print("Dcotor id: ",self.did,'\n',"Patient id:",self.userid,'\n',
              "Patient name:",self.fname,'\n',"Medicince:",self.medicinces)



p= prescription("tablet 1","12","ABC","30")
p.display_pres()

