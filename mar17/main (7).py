def is_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count<3:
        return True
    else:
        return False
    #
    # Write your code here.
    #

for i in range(1, 29):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
