import numpy as np
a=np.array([3,1,2,4])
print(a)
a1=np.array([[1,2,3],[4,5,6]])
print(a1)
a3=np.array([1,2,3,4,5],ndmin=4)# It displays the element surrounded by
# list means the number of list that you have specified 
print(a3)
a4=np.array([10,20,30,40],dtype=complex )
print(a4)
a4=np.array([10,20,30,40],dtype=float )
print(a4)
a4=np.array([10,20,30,40],dtype=bool )
print(a4)
print(a4.shape)
