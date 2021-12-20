a=float(input("Enter your weight"))
b=float(input("Enter Your Height"))
bmi=int(a/(b*b))
if bmi<18.5:
    print("Under Weight ")
elif bmi>=18.5 & bmi<25:
    print("Normal Weight")
elif bmi>=25 & bmi<30:
    print("Over Weight")
elif bmi>=30 &bmi<35:
    print("obese")
else:
    print("Clinicallt obese")
