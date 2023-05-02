string1='My Name is Jessa'
string1list=string1.split(" ")
string2=""
for i in string1list:
    i=str(i)
    string2+=i[::-1]+" "
print(string2.strip())


