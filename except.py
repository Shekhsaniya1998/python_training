#x=int(input("Enter the value of x:"))
try:
    f=open('myfile.txt')
    s=f.readline()
    i=int(s.strip())
except(NameError,ZeroDivisionError,RuntimeError,FileNotFoundError):
    print("There are 3 Exception in this Except:")
# for Except
class B(Exception):
      pass
class C(B):
     pass
class D(C):
     pass
for cls in [B, C, D,L]:
    try:
      raise cls()
    except D:
          print("D")
    except C:
          print("C")
    except B:
          print("B")
