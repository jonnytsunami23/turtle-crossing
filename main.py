import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []

counter = 0



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkeypress(player.move, "Up")
    screen.listen()

    if random.random() < 0.15:
        car = CarManager()
        cars.append(car)
    for car in cars:
        car.move()
        if car.hit_turtle(player):
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.restart()
        scoreboard.update_score()
        for car in cars:
            car.speed_up()




screen.exitonclick()
