truecount=0
name1=input("Enter your name !")
name1=name1.lower()
name2=input("Enter your Lover name !")
name2=name2.lower()
name1+=name2
truecount+=name1.count("t");
truecount+=name1.count("r");
truecount+=name1.count("u");
truecount+=name1.count("e");

truecount=truecount*10

truecount+=name1.count("l");
truecount+=name1.count("o");
truecount+=name1.count("v");
truecount+=name1.count("e");

print(f"your love score is {truecount}")

