import numpy as np
a=np.arange(0,60,5)
a=a.reshape(3,4)
print("Orginal array")
print(a)
print('\n')
print("Modifies array is")
for x in np.nditer(a):
    print(x)


b=a.T
print("Transpose of array")
print(b)
