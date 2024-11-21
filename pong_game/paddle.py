from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.position)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 40)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 40)

