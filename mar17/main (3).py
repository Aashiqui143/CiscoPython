my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newlist=[]
#
# Write your code here.
#
print("The list with unique elements only:")
for i in my_list:
    if i not in newlist:
         newlist.append(i)
print(newlist)

