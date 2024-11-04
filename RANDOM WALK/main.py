
from turtle import Turtle,Screen
import random as r
#player input
players=int(input("ENTER NUMBER OF PLAYERS:"))
n_players=[]
for player in range(players):
    new_player=int(input(f"GUESS THE COUNT PLAYER {player+1}:"))
    n_players.append(new_player)
max_c=max(n_players)
player_n=n_players.index(max_c)+1
#RANDOM WALK
s=Screen()
t=Turtle()

s.colormode(255)

direction=[0,90,180,270]
c=0
walk=True
while walk:
    R = r.randint(0, 255)
    G = r.randint(0, 255)
    B = r.randint(0, 255)
    T = (R, G, B)
    t.speed(8)
    s.bgcolor("lightblue")
    s.title("RANDOM WALK")
    s.setup(width=500, height=500)
    t.color(T)
    t.pensize(10)
    t.forward(30)
    t.setheading(r.choice(direction))
    x,y=t.position()
    c+=1
    if abs(x)<1 and abs(y)<1:
        print("COUNT : ",c)
        walk=False
        print("TURTLE CAME BACK !.\nDRAW MATCH :)")
        s.exitonclick()

    if abs(y)>-240 and abs(y)>240:
        print("COUNT : ", c)
        walk=False
        print("TURTLE HAS EXITED THE LIMIT !.")
        print(f"THUS PLAYER {player_n+1} WINS THE GAME !.\nPLAYER COUNT:{max_c}.")
        s.exitonclick()
    if abs(x)>-235 and abs(x)>235:
        print("COUNT : ", c)
        walk=False
        print("TURTLE HAS EXITED THE LIMIT !.")
        print(f"THUS PLAYER {player_n} WINS THE GAME !.\nPLAYER COUNT:{max_c}.")
        s.exitonclick()
