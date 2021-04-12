dict={"Name" :"saniya","Age":23,"Class":"Frist"}
print(dict)
print(dict['Name'])
dict['Name']="shekh"
print(dict)
dict["Name"]="SANIYA"
print(dict)
dict["BFF"]="Thousif"
print(dict)
print(dict['BFF'])
dict['AgeT']=27
print(dict)
del dict['BFF']
print("After delete",dict)
del dict['AgeT']
print("After delete",dict)
dict.clear()
print(dict)
del dict
print(dict)
print(type(dict))
