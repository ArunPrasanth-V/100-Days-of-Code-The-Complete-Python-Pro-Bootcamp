import random
print("Welcome to the Game ! ")
print("Find the one  Number between 1 to 100  i had guessed !")
level=int(input("Choose the difficulty Level 'Hard'-> 1 : 'Easy'-> 0  "))
if level==1:
    attempt=5
    print("Your choosing Hard level your attempt is 5 ")
else:
    attempt=10
    print("Your choosing Easy level your attempt is 10 ")
find_number=random.randint(1,101)
bool=False
for i in range(attempt):
    num=int(input("Enter the Number :  "))
    if(num==find_number):
        bool=True
        print(f"YOU WIN !! with {attempt-(i-1)} attempt Remaining")
    elif(num>find_number):
        print(f"Entered Number is Too High .. Attempt Remaining : {attempt-(i+1)} ")
    else:
        print(f"Entered Number is Too Low .. Attempt Remaining : {attempt-(i+1)} ")

if not bool:
    print("You Lose ..")
