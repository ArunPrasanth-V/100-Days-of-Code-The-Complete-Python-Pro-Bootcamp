from turtle import Screen
import time
from snack import Snack
from food import Food
from scoreboard import ScoreBorad
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0)

snack = Snack()
food = Food()
scoreboard=ScoreBorad()

screen.listen()
screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.left, "Left")
screen.onkey(snack.right, "Right")
is_gameOn = True
while is_gameOn:
    screen.update()
    time.sleep(0.1)
    snack.mov()

    # Detect collision with food.
    if snack.head.distance(food) < 15:
        food.refresh()
        snack.extend()
        scoreboard.increase_score()
    # Detect collision with wall.
    if snack.head.xcor()>300 or snack.head.xcor()<-290 or snack.head.ycor()>300  or snack.head.ycor() < -300:
        is_gameOn=False
        scoreboard.game_over()

    # Detect collision with tail.
    for seg in snack.segment[1:]:
        if snack.head.distance(seg) < 10:
            is_gameOn = False
            scoreboard.game_over()


screen.exitonclick()
