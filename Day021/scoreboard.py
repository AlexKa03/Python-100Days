from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
MOVE = False


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=MOVE, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over", align=ALIGNMENT, font=FONT)
