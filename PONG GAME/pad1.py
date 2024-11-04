from turtle import Turtle
class Pad1(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(5, 1)
        self.goto((350, 0))
        self.move_up()
        self.move_down()

    def move_up(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)

    def move_down(self):
        y=self.ycor()-20
        self.goto(self.xcor(),y)
