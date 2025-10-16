from turtle import Turtle, Screen
from random import choice
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(244, 240, 232), (214, 154, 105), (49, 96, 139), (163, 80, 45), (223, 209, 107), (17, 36, 59), (185, 163, 25), (120, 163, 202), (56, 30, 18), (126, 68, 94), (210, 91, 69), (43, 128, 70), (193, 140, 160), (162, 20, 10), (125, 181, 156), (129, 26, 42), (19, 52, 43), (194, 91, 113), (48, 170, 98), (39, 62, 97), (27, 91, 52), (235, 162, 187), (108, 118, 172), (225, 206, 2), (6, 88, 108), (227, 179, 170)]

tim = Turtle()
screen = Screen()
screen.setup(600, 580)
screen.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed(0)
tim.goto(-235,-220)
tim.pendown()

for row in range(10):
    for col in range(10):
        tim.dot(20, choice(color_list))
        coordinates = tim.pos()
        tim.penup()
        tim.goto(coordinates[0] + 50, coordinates[1])
        tim.pendown()

    coordinates = tim.pos()
    tim.penup()
    tim.goto(coordinates[0] - 500, coordinates[1] + 50)
    tim.pendown()

screen.exitonclick()