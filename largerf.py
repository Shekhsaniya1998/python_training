def larger(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
print("The largest of Three numbers is ",larger(20,10,30))
