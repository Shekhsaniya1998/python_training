dict={"Name":"Thousif","Age":27}
dict1={"Name":"Saniya","Age":23}
dict2={}
#print(cmp(dict,dict1))
x=dict.keys()
print(x)
y=dict1.keys()
print(y)
p=dict1.values()
print(p)
m=dict.items()
print(m)
'''if "Name" in dict:
    print("True")

else:
    print("No")'''
print(len(dict))
    
dict["Location"]="Bangalore"
print(dict)
print(str(dict))
print(len(dict))
#dict.fromkeys()
#dict.haskey("Name")
dict2.update(dict)
print(dict2)
