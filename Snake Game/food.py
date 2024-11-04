from turtle import Turtle
import random as r

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
    #random position of food
    def refresh(self):
        x = r.randint(-230, 240)
        y = r.randint(-230, 240)
        self.goto(x, y)

