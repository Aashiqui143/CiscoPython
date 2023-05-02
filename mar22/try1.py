from math import *
list1=[1,2,3,4,5]
list2=[100, 200, 300, 400, 500]
#list2.reverse()
list3=list1+list2
#for i , j in zip(list1, list2):
    #print(i , j)
print(list3)

for i in range((len(list3))//2):
    print(list3[i],list3[-i-1])

list4=[1,2,3,4]
del list4[3]
print(list4)
print(factorial(5))