from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.obstacles = []
        self.speed = STARTING_MOVE_DISTANCE

    def obstacle_spawner(self):
        chance = random.randint(1, 6)
        if chance == 6:
            pos_y = random.randint(-230, 240)
            new_obstacle = Turtle()
            new_obstacle.penup()
            new_obstacle.shape("square")
            new_obstacle.shapesize(stretch_wid=1, stretch_len=2)
            new_obstacle.color(random.choice(COLORS))
            new_obstacle.goto(300, pos_y)
            self.obstacles.append(new_obstacle)


    def go_up(self):
        for obstacle in self.obstacles:
            obstacle.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
