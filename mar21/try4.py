import random
list1=[random.randrange(5) for i in range(20)]
print(list1)
newdict=dict()
for elem in list1:
    newdict[elem]=list1.count(elem)
print(newdict)
