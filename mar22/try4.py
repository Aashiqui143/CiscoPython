a='''for i in range({}):
    print(str(i+1)*(i+1))'''.format(5)
print(a)
user=input("Enter a number = ")
if user==user[::-1]:
    print("Given number \"{}\" is a palindrome".format(user))
else:
    print("Given number {} is NOT a palindrome".format(user))