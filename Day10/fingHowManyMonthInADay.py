def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            True
    else:
        return False
def day_in_month(year,months):
    month=[0,31,28 , 31 ,30, 31, 30, 31 , 31 , 30 , 31 ,30 ,31]
    if months==2&leap_year(year):
        return 29
    return month[months]
year=int(input("Enter the Year"))
month=int(input("Enter the Month : "))
print(day_in_month(year,month))
