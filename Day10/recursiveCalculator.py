
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b

def selection(symbol,a,b):
    if symbol == "+":
        return add(a, b)
    elif symbol == "-":
        return sub(a, b)
    elif symbol == "*":
        return mul(a, b)
    else:
        return div(a, b)
ans=0
a=int(input("Enter the Value : "))
symbol = input("Choose Your Option \n + \n - \n * \n / ")
b=int(input("Enter the Value : "))
num=selection(symbol,a,b)
print(a,"  ",symbol,"",b," = ",num)

y="y"
y = input("Do you Want to Continue 'y' else 'n' ")
while(y=="y"):
    symbols = input("Choose Your Option \n + \n - \n * \n / ")
    aa = int(input("Enter The Number : "))
    num = selection(symbols, num, aa)
    print(num, "  ", symbols, "", aa, " = ", num)
    y=input("Do you Want to Continue 'y' else 'n' ")
