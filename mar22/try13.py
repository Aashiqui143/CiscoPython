sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
li2=[]
for i in sample_list:
    if sample_list.count(i)>1:
        li2.append(i)

set1=set(li2)
print(set1)
    