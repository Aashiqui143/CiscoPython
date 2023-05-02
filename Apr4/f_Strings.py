line="My name is {} and I am from {}"
print(line.format('Ashiq','India'))
print('Ashiq'[0])
x=123
print(f'I have {type(x)} dollors')

# This is for *args
def sum1(*par):
    sum=0
    for i in par:
        sum+=i
    return sum
print(sum1(3,5,6,7,85,7))

# This is for **kwargs
def display_name(**kwargs):
    print("Hello,", end=" ")
    for value in kwargs.values():
        print(value,end=" ")
    print("")

display_name(first="Zindesha",middle="Ashiq",last="Syed") 