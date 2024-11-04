from turtle import Screen,Turtle
from pad1 import Pad1
from pad2 import Pad2
from ball import Ball
from score1 import Score1
from score2 import Score2

import time as t
#screen
s=Screen()
s.listen()
s.setup(width=800,height=600)
s.title("PONG GAME ")
s.bgcolor("black")
s.tracer(0)
p1=Pad1()
p2=Pad2()
b=Ball()
s1 =Score1()
s2=Score2()
l=Turtle()
l.color("white")
game=True
while game:
    #pausing the while loop
    t.sleep(0.030)
    s.update()

    #centre line and border for score
    l.penup()
    l.goto(0, 300)
    l.pendown()
    l.goto(0, -300)
    l.penup()
    l.goto(-400,260)
    l.pendown()
    l.goto(400,260)

    #moving ball
    b.move_ball()

    #key movements
    s.onkeypress(p1.move_up, "Up")
    s.onkeypress(p1.move_down, "Down")
    s.onkeypress(p2.move_up, "w")
    s.onkeypress(p2.move_down, "s")

    #reset the position if exit by x
    if b.xcor() > 380:
        # increase score for P1
        s2.increase_score()
        #rest
        b.reset_pos()

    # reset the position if exit by -x
    if b.xcor() < -380:
        # increase score for P2
        s1.increase_score()
        #reset
        b.reset_pos()


    #bounce in the up bottom wall
    if b.ycor() > 250 or b.ycor() < -280:
        b.ybounce()

    #bounce upon the paddles
    if b.distance(p1) < 50 and b.xcor() > 320 or b.distance(p2) < 50 and b.xcor() < -320:
        b.xbounce()
s.exitonclick()