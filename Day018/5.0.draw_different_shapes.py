from turtle import Turtle, Screen
import random

def draw(times, arrow):
    angle = 360 / shape

    for side in range(times):
        arrow.right(angle)
        arrow.forward(120)

shapes = [3, 4, 5, 6, 7, 8, 9, 10]

timmy = Turtle()
screen = Screen()

timmy.pensize(2)

for shape in shapes:
    screen.colormode(255)
    timmy.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    draw(shape, timmy)

screen.exitonclick()
