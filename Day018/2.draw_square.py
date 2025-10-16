from turtle import Turtle, Screen

def draw_side(turtle):
    turtle.forward(100)
    turtle.right(90)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
for side in range(4):
    draw_side(timmy_the_turtle)

screen = Screen()
screen.exitonclick()
