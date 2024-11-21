from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0

    def display_scores(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.left_score}",align= "center",font= ("Courier",80,"normal"))
        self.goto(100,200)
        self.write(f"{self.right_score}",align= "center",font= ("Courier",80,"normal"))

    def increment_left_score(self):
        self.left_score += 1

    def increment_right_score(self):
        self.right_score += 1
