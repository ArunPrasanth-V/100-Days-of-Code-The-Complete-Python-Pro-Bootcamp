payer={}
def winner():
    amounts=0
    name=""
    for i in payer:
        valuse=payer[i]
        if valuse>amounts:
            amounts=payer[i]
            name=i
    print(f"The Winner is {name} with ${amounts}")
bool = True
while(bool):
    name = input("Enter Your Name :  ")
    amount=int(input("Enter the Amount $ : "))
    payer[name] = amount
    b=input("Is anyone is available 'yes' else 'no' : ")
    if b=="yes":
        bool=True
    else:
        bool=False
winner()
