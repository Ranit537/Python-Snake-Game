from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))

    def score(self,c):
        self.clear()
        self.write(f"Score: {c}", align="center", font=("Arial", 10, "normal"))