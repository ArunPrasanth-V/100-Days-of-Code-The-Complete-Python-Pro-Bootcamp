from turtle import Turtle
import random
COLOR=["red","orange","yellow", "blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOV_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_car=[]

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance ==1 :
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOR))
            random_y = random.randint(-250, 250)
            new_car.goto(380, random_y)
            self.all_car.append(new_car)


    def move_car(self):
        for car in self.all_car:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed+=MOV_INCREMENT
