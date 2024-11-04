from turtle import Turtle

class Score1(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        # score count
        self.count = 0
        self.goto(200, 270)
        self.color("white")
        self.hideturtle()
        self.update()
        self.update()

    def update(self):
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 15, "normal"))

    # update the score
    def increase_score(self):
        self.score += 1
        #clear old score
        self.clear()
        # to update current score
        self.update()
