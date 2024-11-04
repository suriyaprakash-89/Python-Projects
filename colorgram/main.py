from turtle import Screen,Turtle
import random as r
t=Turtle()
s=Screen()
'''
import colorgram as c

rgb_colors=[]
colors=c.extract("download.jpeg",10)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)
'''

s.bgcolor("black")
s.colormode(255)
t.penup()
t.hideturtle()
t.speed("fast")
color_list=[(195, 164, 110), (141, 167, 186), (69, 90, 123), (133, 89, 54), (215, 206, 131), (186, 142, 157)]
t.setheading(200)
t.forward(400)
t.setheading(0)
n=100
for i in range(1,n+1):
    t.dot(20,r.choice(color_list))
    t.forward(50)
    if i%15==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(750)
        t.setheading(0)
s.exitonclick()
print("SCREEN CLOSED !")