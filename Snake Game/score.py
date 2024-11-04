from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        #calling turtle inside
        super().__init__()
        self.penup()
        #score count
        self.count = 0
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update()
    #update the score board
    def update(self):
        self.write(f"SCORE: {self.count}", align="center", font=("Arial",15, "normal"))

    #update the score
    def increase_score(self):
        self.count += 1
        #to clear the previous score board
        self.clear()
        #to update current score
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER !", align="center", font=("Arial", 15, "normal"))
