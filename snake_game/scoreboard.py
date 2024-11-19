from turtle import Turtle,Screen

FONT = ("Arial", 18, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.display()


    def display(self):

        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.speed("fastest")
        self.write(f"Score: {self.score} ",align=ALIGNMENT,font=FONT)

    def increment_score(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    score = Scoreboard()


    screen.exitonclick()