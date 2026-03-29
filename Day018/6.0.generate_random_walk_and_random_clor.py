from turtle import Turtle, Screen
import random

possibility = [0, 90, 180, 270]

timmy = Turtle()
timmy.pensize(15)
timmy.speed(0)

screen = Screen()
screen.colormode(255)

for i in range(1000):
    rgb = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    timmy.pencolor(rgb)
    timmy.setheading(random.choice(possibility))
    timmy.forward(30)

screen.exitonclick()
