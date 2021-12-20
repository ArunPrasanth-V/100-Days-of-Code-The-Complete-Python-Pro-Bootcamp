print("Welcome To the Arun Shop's")
a=float(input( "Enter the Amount $ : "))
b=int(input("What percentage of tip you would like to give : ? 10 12 0r 15"))
c=int(input("How Many People ? "))
per=b/100
tip_amount=a*per
total_bill=a+tip_amount
bill=total_bill/c
final_amount=round(bill,2)
print(f"Each person should pay $ {final_amount}" )
