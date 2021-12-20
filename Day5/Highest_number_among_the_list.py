mark=input("Enter the Number ! ").split()
high=0
for i in range(0,len(mark)):
    mark[i]=int(mark[i])
    if high<mark[i]:
        high=mark[i]
print(high)
