from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

INCREMENT_FOR_MOVEMENT = 10

def move_forward():
    tim.forward(INCREMENT_FOR_MOVEMENT)

def move_backward():
    tim.backward(INCREMENT_FOR_MOVEMENT)

def move_left():
    tim.setheading(tim.heading() + INCREMENT_FOR_MOVEMENT)

def move_right():
    tim.setheading(tim.heading() - INCREMENT_FOR_MOVEMENT)

def clear_screen():
    screen.resetscreen()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
