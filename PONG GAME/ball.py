from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()  # Prevent drawing a line
        self.x_move = 6
        self.y_move = 6

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ybounce(self):
        self.y_move *= -1

    def xbounce(self):
        self.x_move*=-1
    def reset_pos(self):
        self.goto(0,0)
        self.x_move*=-1