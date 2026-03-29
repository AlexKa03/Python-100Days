from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy = Turtle()
timmy.speed("fastest")

screen = Screen()
screen.colormode(255)

heading_step = 5

for i in range(0, 360, heading_step):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(i)

screen.exitonclick()
