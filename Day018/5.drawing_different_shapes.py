from turtle import Turtle, Screen
from random import randint

SHAPE_SIDES = [3, 4, 5, 6, 7, 8, 9, 10]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")

for sides in SHAPE_SIDES:
    angle = 360 / sides
    
    r = int(randint(1, 255))
    g = int(randint(1, 255))
    b = int(randint(1, 255))
    tim.pencolor(r, g, b)

    for i in range(sides):
        tim. right(angle)
        tim.forward(100)

screen.exitonclick()