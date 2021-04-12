def add(x,*data,**y):
    # ** keyword argument
    # * variable number of argument
    # output of y will be {}
    # as it is not required
    #if we check it will be tuple
    
    print(x)
    print(y)
    for d in data:
        print(d)
add(1,2,3.4,"ch",'c')
#print(x)
