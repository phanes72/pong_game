from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        # self.setheading(25)

    def move(self, position):
        if self.xcor() < position[0]:
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
