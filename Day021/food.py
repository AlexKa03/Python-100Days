from turtle import Turtle
import random

WIDTH = 0.5
LENGTH = 0.5

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.speed("fastest")
        self.new_location()


    def new_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)
