def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    year=int(year)
    month=int(month)
    day=int(day)
    if year<1582 or month<1 or day<1:
        None
    else:
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        x=is_year_leap(year)
        if x:
            days[1]=29
        total=0
        for i in range(len(days)):
            if month==i+1:
                total+=day
                break
            else:
                total+=days[i]
        return total  

print(day_of_year(2023, 12, 31))
