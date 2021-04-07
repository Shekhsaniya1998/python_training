class Employee:
       empcount=0
       def __init__(self,ename,sal):
           self.ename=ename
           self.sal=sal
           Employee.empcount+=1
       def displayCount(self):
            print ("Total employee %d" %Employee.empcount)
            print(self.ename)
       def displayEmployee(self):
            print("Name :",self.ename,"salary :",self.sal)
    
emp=Employee("saniya",2200)
emp.displayEmployee()
