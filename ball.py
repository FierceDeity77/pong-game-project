from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1  # time.sleep uses this variable

    def ball_move(self):
        rand_x = self.xcor() + self.x_move
        rand_y = self.ycor() + self.y_move
        self.goto(rand_x, rand_y)

    def ball_bounce_y(self):
        self.y_move *= -1

    def ball_bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # increase ball speed when ball contacts with paddle

    def ball_reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.ball_bounce_x()



