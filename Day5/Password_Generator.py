import random
print("Welcome to PyPassword Generator")
letter=int(input("How many letter You Would like to have Password"))
symbol=int(input("How many Symbol's You would like ? "))
number=int(input("how many Number You Would Like ? "))

Letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Number=['0','1','2','3','4','5','6','7','8','9']
Symbol=['!','@','#','$',"%","&","*","(",")"]
pass_list=[]
for i in range(0,letter):
    pass_list+=random.choice(Letter)
for i in range(0,number):
    pass_list+=random.choice(Number)
for i in range(0,symbol):
    pass_list+=random.choice(Symbol)

random.shuffle(pass_list)
password=""
for i in pass_list:
    password+=i
print(password)
