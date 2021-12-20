height=int(input("Enter Your Height"))
if height>=120:
    age=int(input("Enter your age "))
    if age>=19:
        print("Ticket Price $20")
    elif age>=15:
        print("Ticket Price $15")
    else:
        print("Ticket price $7")
else:
    print("You Should be height to get ride")

