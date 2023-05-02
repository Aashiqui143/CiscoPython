def is_year_leap(year):
    #
    # Your code from the previous LAB.
    #
    while year>1580:
       if year%4==0:
           if year%400==0:
               return True
           elif year%100==0:
               return False
           else:
               return True
       else:
            return False
def days_in_month(year, month):
    #
    # Write your new code here.
    #
    da31=[1,3,5,7,8,10,12]
    #da30=[4,6,9,11]
    if month==2:
        x=is_year_leap(year)
        if x:
            return 29
        else:return 28
    else:
        if month in da31:
            return 31
        else:
            return 30
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
