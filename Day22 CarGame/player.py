from turtle import Turtle
STATING_POSITION=(0,-200)
MOV_DISTANCE = 10
FINISH_LINE_Y =280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.go_to_start()
        self.shape("turtle")
        self.setheading(90)

    def go_to_start(self):
        self.goto(STATING_POSITION)

    def mov_up(self):
        self.forward(10)

    def is_at_finish_line(self):
       if self.ycor() >FINISH_LINE_Y:
           return True
       else:
            return False

