from turtle import Turtle,Screen

class Snake:
    def __init__(self):
        # starti ng positions of segments
        self.st_pos = [(0, 0), (-20, 0), (-40, 0)]
        # created segments
        self.segments = []
        self.create_snake()
        self.u=90
        self.d=270
        self.l=180
        self.r=0

    # creating turtle segments
    def create_snake(self):
        for position in self.st_pos:
            self.add_seg(position)

    def add_seg(self,position):
        new_s = Turtle("circle")
        new_s.color("green")
        new_s.penup()
        new_s.goto(position)
        self.segments.append(new_s)

    def extend(self):
        self.add_seg(self.segments[-1].position())
    def move(self):
        # for replacing (3 to 2) and (2 ot 1)
        # at final moving 1 forward
        for n in range(len(self.segments) - 1, 0, -1):
            x = self.segments[n - 1].xcor()
            y = self.segments[n - 1].ycor()
            self.segments[n].goto(x, y)

        # moving 1 forward
        self.segments[0].forward(20)
    def up(self):
        if self.segments[0].heading() != self.d:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != self.u:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != self.r:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != self.l:
            self.segments[0].setheading(360)



