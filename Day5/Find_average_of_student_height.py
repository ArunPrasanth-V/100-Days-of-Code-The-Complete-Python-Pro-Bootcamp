heights=input("Enter the student's Height : ").split(" ")
for i in range(0,len(heights)):
    heights[i]=int(heights[i])
temp=0
for i in heights:
    temp+=i
temp/=len(heights)
print(temp)
