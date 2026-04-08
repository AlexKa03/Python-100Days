from turtle import Turtle

WIDTH = 5
HEIGHT = 1
MOVEMENT = 20

class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.penup()
        self.goto(cords)

    def go_up(self):
        new_y = self.ycor() + MOVEMENT
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - MOVEMENT
        self.goto(self.xcor(),new_y)