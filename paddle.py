from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, goto):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(goto)

    def paddle_r_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_r_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def paddle_l_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_l_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


