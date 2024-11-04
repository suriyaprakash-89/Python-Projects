from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from border import Border
import time
#screen things
s=Screen()
s.setup(600,600)
s.bgcolor("black")
s.title("SNAKE GAME ;)")
s.tracer(0)#for animation
#snake class object
snake=Snake()
#food class object
food =Food()
#score class object
score_board=Score()

#keymovents
s.listen()
s.onkeypress(snake.up,"Up")
s.onkeypress(snake.down,"Down")
s.onkeypress(snake.left,"Left")
s.onkeypress(snake.right,"Right")
#flag
game= True
#moving continuously forward
while game:
    s.update()
    #b.line()
    # border class object
    Border()
    time.sleep(0.1)
    snake.move()
    #snake touching food
    if snake.segments[0].distance(food)<20:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    if snake.segments[0].xcor()>270 or snake.segments[0].xcor()<-270 or snake.segments[0].ycor()>255 or snake.segments[0].ycor()<-255:
        score_board.game_over()
        game=False
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            game=False
            score_board.game_over()


s.exitonclick()


