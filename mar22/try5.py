user=int(input("Enter a num = "))
user=str(user)
for i in range(len(user)):
    print(user[-i-1], end=" ")
