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
