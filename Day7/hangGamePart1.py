import random
name=["arun","varun","javaProgrammer"]
findingName=random.choice(name)
newlist=[]
for i in range(0,len(findingName)):
    newlist.append("_")
getchar=input("Guess a Letter :")
index=0
for element in findingName:
    if getchar in element:
       newlist[index]=element
    index+=1
print(newlist)
