import numpy as np
list1=[1,2,[4,6,8,[34,76,32,[67,98],54,76],78,90],54,32]
list3=[]
def combineList(list1):
    for i in list1:
        if type(i) is list:
            combineList(i)
        else:
            list3.append(i)
    return list3
x=combineList(list1)
x=np.array(x)
print(x,type(x))
