from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid= 1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.penup()

        self.goto(300, random.randint(-150,150))
        self.setheading(180)
        self.car_speed = STARTING_MOVE_DISTANCE
    def move(self):
        self.forward(self.car_speed)
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

    def hit_turtle(self, player):
        if self.distance(player) < 30:
            return True

