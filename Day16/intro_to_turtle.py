from turtle import Turtle, Screen


def mov_that():
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)


timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.pencolor("red")

for i in range(4):
    mov_that()

turtle_screen = Turtle.Screen()
turtle_screen.canvheight
turtle_screen.exitonclick()
