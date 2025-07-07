from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

is_on = True
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turns the animation off but needs to update manually

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))  # put in a tuple to pass 2 arguments to a single variable
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.paddle_r_up, "Up")
screen.onkey(r_paddle.paddle_r_down, "Down")
screen.onkey(l_paddle.paddle_l_up, "w")
screen.onkey(l_paddle.paddle_l_down, "s")

while is_on:
    screen.update()  # updates the screen
    time.sleep(ball.move_speed)  # sleep between the screen updates
    ball.ball_move()

    # detect collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.ball_bounce_x()

    # detect if the ball goes beyond the screen
    if ball.xcor() > 380:
        ball.ball_reset_position()
        scoreboard.add_l_score()

    # left paddle
    if ball.xcor() < -380:
        ball.ball_reset_position()
        scoreboard.add_r_score()


screen.exitonclick()
