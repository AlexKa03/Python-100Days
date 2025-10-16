from turtle import Turtle, Screen
from random import choice, randint

DIRECTION = [0, 90, 180, 270]

def random_color(turtle):
    r = int(randint(1, 255))
    g = int(randint(1, 255))
    b = int(randint(1, 255))
    turtle.color(r, g, b)

def move_turtle(turtle):
    turtle.setheading(chosen_direction)
    turtle.forward(30)

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.width(15)
tim.speed(0)

for _ in range(200):
    chosen_direction = choice(DIRECTION)
    random_color(tim)
    move_turtle(tim)

screen.exitonclick()
