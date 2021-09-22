from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(starting_position)
        self.speed("fastest")

    def up(self):
        new_y = self.ycor() + 20
        x = self.xcor()
        self.goto(x, new_y)

    def down(self):
        new_y = self.ycor() - 20
        x = self.xcor()
        self.goto(x, new_y)
