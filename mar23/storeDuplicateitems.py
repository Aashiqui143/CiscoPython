list1=[1,2,3,4,1,2,6,7,3,6,4,8,2,1]
set1=set()
dup=set()
for i in list1:
    if i not in set1:
        set1.add(i)
    else:
        dup.add(i)
dup=list(set(dup))
print(dup)
