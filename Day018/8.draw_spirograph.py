from turtle import Turtle, Screen
from random import randint

def random_color(turtle):
    rgb_tuple = (randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.color(rgb_tuple)

def draw(turtle, gap):
    for i in range(0, 360, gap):
        random_color(tim)
        turtle.circle(100)
        turtle.setheading(i)

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)

draw(tim, 5)

screen.exitonclick()
