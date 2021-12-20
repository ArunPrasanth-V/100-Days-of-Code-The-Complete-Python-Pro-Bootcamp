height=int(input("Enter Your Height"))
ticket=0;
if height>=120:
    age=int(input("Enter your age "))
    if age>=19:
        ticket=20
    elif age>=15:
        ticket=15
    else:
        ticket=7
    bool=int(input("Do you want to take PHOTO press 1 for Yes"))
    if bool==1:
        ticket=ticket+5;
    print(f"Your Total Ticket Price is ${ticket} /-")
else:
    print("You Should be height to get ride")
