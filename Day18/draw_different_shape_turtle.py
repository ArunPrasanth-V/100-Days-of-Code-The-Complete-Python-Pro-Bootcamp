import random
import turtle as t
import turtle

# Dashed Line
# tim=t.Turtle()
# for i in range(10):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
#


# Hexagen
# tik=t.Turtle()
color = ["green yellow", "chartreuse", "lawn green", "lime", "yellow green", "olive drab"]


# for number_of_side in range(3,11):
#     for _ in range(number_of_side):
#         tik.color(random.choice(color))
#         angle = 360 / number_of_side
#         tik.forward(100)
#         tik.right(angle)


# random Walk
def random_color():
    r =int(random.randint(0, 255))
    g =int(random.randint(0, 255))
    b =int(random.randint(0, 255))
    c=(r, g, b)
    return c

#
# timmy = t.Turtle()
# t.colormode(255)
# direction = [0, 90, 180, 170]
# timmy.pensize(15)
# timmy.speed("fastest")
# for _ in range(50):
#     timmy.color(random_color())
#     timmy.backward(30)
#     timmy.setheading(random.choice(direction))


#spirography
timmy=t.Turtle()
t.colormode(255)
timmy.speed("fastest")
def size_of_gap(size):
    for _ in range(int(360/size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size)

size_of_gap(5)
screen = turtle.Screen()
screen.exitonclick()


