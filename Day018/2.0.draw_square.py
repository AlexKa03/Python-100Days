from turtle import Turtle, Screen

def draw_square(turtle):
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.color("green")

draw_square(timmy)

screen.exitonclick()
