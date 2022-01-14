import turtle
from turtle import Turtle, Screen
import random
is_raceOn=False
screen = Screen()
# For DialogBox
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make Your bet ",prompt="Which turtle will win the race? Enter the color : ")
color=["red","orange","yellow","green","blue","purple"]
y_position=[-100,-50,0,50,100,150]
all_turtle=[]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_raceOn=True

while is_raceOn:
    if turtle.xcor()>230:
        winning_color=turtle.pencolor()
        is_raceOn=False
        if(user_bet==winning_color):
            print(f"You're won! {winning_color} turtle is the winner!")
        else:
            print(f"You're lost! {winning_color} turtle is the winner!")
    for turtle in all_turtle:
        turtle.forward(random.randint(0, 10))





screen.exitonclick()
