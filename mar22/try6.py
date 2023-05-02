user=int(input("Enter income = "))
tax=0
if user<=10000:
    print("Tax = zero")
elif user>10000 and user<=20000:
    tax=user-10000
    tax=tax*0.1
    tax=int(tax)
    print("Tax = $"+str(tax))
elif user>20000:
    tax=user-20000
    tax=10000*0.1 + tax*0.2
    tax=int(tax)
    print("Tax = $"+str(tax))