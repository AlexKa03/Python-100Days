from turtle import Turtle, Screen

def draw_line(turtle):
    turtle.forward(6)
    turtle.penup()
    turtle.forward(6)
    turtle.pendown()

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
for side in range(50):
    draw_line(timmy_the_turtle)

screen = Screen()
screen.exitonclick()
