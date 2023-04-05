from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.refresh()
        self.color(random.choice(COLORS))

    def refresh(self):
        self.goto(random.randrange(-280,280, 20),random.randrange(-255,280, 20))

    def level_up(self):
        global MOVE_INCREMENT
        MOVE_INCREMENT *= 1.3

    def move(self):
        self.forward(MOVE_INCREMENT)

    def go_back(self):
        self.goto(320,random.randrange(-255,280,20))

    def start_car(self):
        self.go_back()





