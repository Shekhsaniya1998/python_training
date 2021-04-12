import numpy as np

student=np.dtype([('name','S30'),('age','i1'),('marks','f4')])
a=np.array([('abc',12,10.5),('def',10,12.5)],dtype = student)
print(a)
student1=np.dtype([('fname','S30'),('LOC','S30'),('Phone','i4')])
a1=np.array([('saniya','tumukur','984')],dtype=student1)
print(a1)
stu=np.dtype([('nam','S30'),('add','S30')])
b=np.array([('sani','bnglr')],dtype=stu)
print(b)
print(b.shape)
print(a.shape)
