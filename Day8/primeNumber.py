num=int(input("Enter the Number : "))
bool=False
for i in range(2,num):
    if num%i==0:
        bool=True
        break
if bool:
    print("Not a Prime Number!! ")
else:
    print("Prime Number !! ")
