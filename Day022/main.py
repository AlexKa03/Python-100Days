# Make a class for the paddles, one will be on the left the other will be on the right. They are separate instances, so they will be operated with different keybindings
#
# Draw a dashed line in the middle screen, to separate the players areas
#
# Draw the ball that will be passed between the paddles and will bounce  if it touches the top or bottom part of the screen.
#
# Track Score for both players
#
# Count point if paddles misses the ball, if left paddle misses the ball, +1 point for the player on the right, if opposite count +1 point for the left one.

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(False)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right_paddle and left_paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320
            or ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()