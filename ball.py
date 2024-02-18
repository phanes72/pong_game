from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.xcor()
        self.ycor()
        self.x_move = 0.2
        self.y_move = 0.2
        self.ball_speed = 0.001

    def move(self, position):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

        if self.ycor() > 300:
            self.sety(290)
            self.y_move *= -1

        if self.ycor() < -300:
            self.sety(-290)
            self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.ball_speed = 0.001
