dict={
    1:"one",
    2:"Two",
    3:"Three"
    }
print(1 in dict)
print(4 not in dict)
print(2 not in dict)

paris={
    1:"apple",
    "orange":[2,3,4],
    True:False,
    None:"True"
    }
print(paris.get("orange"))
print(paris.get(True))
print(paris.get(2),"Not in Dict")
