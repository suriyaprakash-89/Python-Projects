from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        #self.line()
        #def line(self):
        self.color("red")
        self.shape("square")
        self.penup()
        self.goto(-270, 250)
        self.pendown()
        self.pensize(2)
        self.goto(-270,250)
        self.goto(270,250)
        self.goto(270,-250)
        self.goto(-270,-250)
        self.goto(-270,250)
        self.hideturtle()



