first_list = [2, 3, 4, 5, 6, 7, 8,2]
second_list = [4, 9, 16, 25, 36, 49, 64,4]

set1=[]
for i in range(len(first_list)):
    z=(first_list[i],second_list[i])
    set1.append(z,)
set1=set(set1)
print(set1)