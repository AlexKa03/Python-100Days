from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(position=(350, 0))
left_paddle = Paddle(position=(-350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    # Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle missed
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect L paddle missed
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()
