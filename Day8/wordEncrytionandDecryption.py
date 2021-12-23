def encryption(txt,shift):
    string=""
    for element in txt:
        string+=chr(ord(element)+shift)
    print(string)

def decryption(txt,shift):
    string=""
    for element in txt:
        string+=chr(ord(element)-shift)
    print(string)


direction=input("Type encode to encrypte & Type Decode to decrypte : ")
txt=input("Type Your Message : ")
shift=int(input("Type the Shift Number : "))
if "de"in direction:
    decryption(txt,shift)
else:
    encryption(txt,shift)

