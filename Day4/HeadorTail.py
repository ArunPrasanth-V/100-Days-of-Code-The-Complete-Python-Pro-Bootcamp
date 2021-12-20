import random
num=int(input("Enter the seed number ! "))
num=random.seed(num)
if num%2==0:
    print("Tail")
else:
    print("Head")
