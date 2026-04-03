from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_clockwise():
    current_heading = tim.heading()
    tim.setheading((current_heading - 10) % 360)

def turn_counterclockwise():
    current_heading = tim.heading()
    tim.setheading((current_heading + 10) % 360)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_counterclockwise, key="a")
screen.onkey(fun=turn_clockwise, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
