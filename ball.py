from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(35)

    def move(self, position):
        if self.xcor() < position[0]:
            self.forward(20)
