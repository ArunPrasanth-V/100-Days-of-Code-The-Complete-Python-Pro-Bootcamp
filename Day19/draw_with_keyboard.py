from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_back():
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() - 10)


def turn_right():
    tim.setheading(tim.heading() + 10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.penup()


screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Down", fun=move_back)
screen.onkey(key="Left", fun=turn_right)
screen.onkey(key="Right", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
