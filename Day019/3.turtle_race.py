from random import randint
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle would win the race? Enter a color: ")
colors = ["red", "orange", "purple", "green", "blue", "violet"]
y_axis = [-100, -60, -20, 20, 60, 100]
turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y_axis[index])
    turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")

        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
