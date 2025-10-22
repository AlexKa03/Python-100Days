import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Crossing Game")

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    new_car = car_manager.obstacle_spawner()
    car_manager.go_up()

    # Detect collision with car
    for obstacle in car_manager.obstacles:
        if turtle.distance(obstacle) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect crossing from turtle
    if turtle.is_at_finish():
        turtle.to_spawn()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
