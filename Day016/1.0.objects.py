# import another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue") # Pause 1 - how to change color
timmy.forward(100) # Pause 2 - how to move the turtle by 100 paces

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
