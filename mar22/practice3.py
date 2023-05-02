str_x = "Emma is good developer. Emma is a writer"
strlist=str_x.split(" ")
print(strlist)
strdict=dict()
for i in strlist:
    strdict[i]=strlist.count(i)
print(strdict)
nam=input("Enter substring = ")
print(strdict[nam])
