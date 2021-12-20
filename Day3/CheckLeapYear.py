year=int(input("Enter the Year"))
if year%4==0:
    if year%100!=0:
        print("Leap Year")
    else:
        if year%400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
else:
    print("Not a Leap Year")
