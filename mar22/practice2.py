string1="pynative"
string2=""
n=int(input("Enter a num = "))
count=0
for i in range(len(string1)):
    if i<n:
        pass
    else:
        string2+=string1[i]
print(string2)