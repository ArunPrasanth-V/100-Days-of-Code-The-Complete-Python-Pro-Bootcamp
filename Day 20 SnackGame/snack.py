from turtle import Turtle, Screen

STRING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snack:
    def __init__(self):
         self.segment = []
         self.create()
         self.head =self.segment[0]

    def create(self):
        for i in STRING_POSITION:
            self.add_segment(i)

    def add_segment(self,position):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.goto(position)
        self.segment.append(new_turtle)


    def extend(self):
        # Add new segment to snack.
        self.add_segment(self.segment[-1].position())



    def mov(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
