size=input("DO YOU WANT S or M or L PIZZA")
price=0
if size=="S"or size=="s":
    price+=15
elif size=="M"or size=="m":
    price+=20
else:
    price+=25
pepper=input("Do you want to add pepperoni !! Y or N")
if pepper=="Y"or pepper=="y":
    if size=="S"or size=="s":
        price+=2
    else:
        price+=3
cheeze=input("Do You want extra cheeze !! Y or N")
if cheeze=="Y"or cheeze=="y":
    price+=1

print(f"Total Price for PIZZA is ${price} ")

