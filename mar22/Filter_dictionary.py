d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

l1 = ['A', 'C', 'F']
newdict=dict()
for i in d1:
    if i in l1:
        newdict[i]=d1[i]
print(newdict)