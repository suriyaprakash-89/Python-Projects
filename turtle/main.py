import random as r
from traceback import print_tb
from turtle import Turtle, Screen

t = Turtle()

s = Screen()
#CIRCLE
'''
for steps in range(100):
    for c in ("blue","green","white"):
        speed("fastest")
        color(c)
        forward(steps)
        right(30)
'''
#SQUARE
'''
turtle.speed(1)
turtle.forward(100)
turtle.speed(9)
turtle.right(90)
turtle.speed(1)
turtle.forward(100)
turtle.speed(1)
turtle.right(90)
turtle.speed(1)
turtle.forward(100)
turtle.speed(1)
turtle.right(90)
turtle.speed(1)
turtle.forward(100)
'''
#DOTTED LINE
'''

for _ in range(10):
    t.forward(10)
    t.pendown()
    t.forward(10)
    t.penup()

'''
#SHAPES

'''
colour=["orange","yellow","red","green","pink","brown","blue"]

def shape(num_sides):

    angle=360/num_sides

    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

k = 0
for shape_side_n in range(3,11):

    t.color(colour[k])
    shape(shape_side_n)
    k += 1
'''

#RANDOM WALK
'''
direction=[0,90,180,270]
c=0
while True:
    R = r.randint(0, 255)
    G = r.randint(0, 255)
    B = r.randint(0, 255)
    T = (R, G, B)
    t.speed(8)
    s.bgcolor("lightblue")
    s.title("RANDOM WALK")
    s.setup(width=800, height=600)
    t.color(T)
    t.pensize(10)
    t.forward(30)
    t.setheading(r.choice(direction))
    x,y=t.position()
    c+=1
    if abs(x)<1 and abs(y)<1:
        print("COUNT : ",c)
        break
        print("TURTLE CAME BACK !")
'''
#spirograph
'''
t.speed("fastest")
a=t.heading()
s.colormode(255)
while True:
    R = r.randint(0, 255)
    G = r.randint(0, 255)
    B = r.randint(0, 255)
    T = (R, G, B)
    t.color(T)
    t.circle(100)
    t.setheading(t.heading()+5)
    x,y=t.position()
    if t.heading()==a:
        break
s.exitonclick()

'''
#KEY MOVEMENTS
'''
def move_forward():
    t.forward(10)
def move_backward():
    t.backward(10)
    t.pencolor("green")
def move_right():
    t.right(10)
    t.pencolor("yellow")
def move_left():
    t.left(10)
    t.pencolor("blue")
def clear_screen():
    s.reset()
s.listen()
t.shape("turtle")
t.color("black")
t.pencolor("red")
s.onkeypress(move_forward,"w")
s.onkeypress(move_backward,"s")
s.onkeypress(move_right,"d")
s.onkeypress(move_left,"a")
s.onkeypress(clear_screen,"r")
s.exitonclick()
'''
#turtle race

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
input = s.textinput("BET ON A TURTLE", "ENTER TURTLE COLOR:")
t1.penup()
t2.penup()
t3.penup()
t4.penup()
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
s.setup(500, 400)
s.title("TURTLE RACE")
t1.color("purple")
t2.color("red")
t3.color("orange")
t4.color("green")
s.bgcolor("black")
t1.goto(-240, 100)
t2.goto(-240, 30)
t3.goto(-240, -30)
t4.goto(-240, -100)
game = False
players=[t1,t2,t3,t4]
if input:
    game=True
while game:
    for player in players:
        n = r.randint(1, 10)
        player.forward(n)
        if player.xcor()>220:
            game=False
            winner=player.pencolor()
            if input==winner:
                print(f"YOU WON !{winner} WINS THE RACE ;)")
            else:
                print(f"YOU LOST !{winner} WINS THE RACE :)")

s.exitonclick()


