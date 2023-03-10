from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
       

    def score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("courier",80,"normal"))


    def l_score_increase(self):
        self.l_score += 1
    
    def r_score_increase(self):
        self.r_score += 1
