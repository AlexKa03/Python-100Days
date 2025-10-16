from turtle import Turtle, Screen
from random import choice, randint

DIRECTION = [0, 90, 180, 270]

def random_color(turtle):
    rgb_tuple = (randint(0, 255), 
                 randint(0, 255), 
                 randint(0, 255)) # THE TUPLE
    turtle.color(rgb_tuple)

def move_turtle(turtle):
    turtle.setheading(chosen_direction)
    turtle.forward(30)

tim = Turtle()
screen = Screen()
screen.colormode(255) # I BROKE MY HEAD BEFORE I LEARNED FROM THE DOCS THAT THIS IS NEEDED FOR RGB
tim.width(15)
tim.speed(0)

for _ in range(200):
    chosen_direction = choice(DIRECTION)
    random_color(tim)
    move_turtle(tim)

screen.exitonclick()
