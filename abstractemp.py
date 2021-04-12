from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, empid, empname,basic, hra):
        self.id = empid
        self.name = empname
        self.basic = basic
        self.hra = hra

    @abstractmethod
    def calcSal(self):
        pass
class Developer(Employee):
    def __init__(self, empid, empname,basic, hra,skillall):
        super().__init__(empid, empname,basic, hra)
        self.skillall = skillall
    def calcSal(self):
        return self.basic+self.hra+self.skillall

class Manager(Employee):
    def __init__(self, empid, empname,basic, hra,bonus):
        super().__init__(empid, empname,basic, hra)
        self.bonus = bonus
    def calcSal(self):
        return self.basic+self.hra+self.bonus

emp = Developer(5000,"Gnaehs", 2222,222,1000)
print("The salary of developer is :",emp.calcSal())
emp1 = Manager(5000,"Gnaehs", 2222,222,100)
print("The salary of Manager is :",emp1.calcSal())
