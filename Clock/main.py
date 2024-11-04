from turtle import *
import turtle
import time

# Set up the screen
ws = turtle.Screen()
ws.bgcolor("black")
ws.setup(width=600, height=600)
ws.tracer(00)  # Turn off automatic screen updates

# Set up the turtle
tur = turtle.Turtle()
tur.hideturtle()
tur.speed(0)
tur.pensize(3)


# Function to draw the clock
def draw_clock(hour, minute, second, tur):
    tur.up()
    tur.goto(0, 210)
    tur.setheading(180)
    tur.color("red")
    tur.pendown()
    tur.circle(210)

    # Draw clock ticks
    tur.up()
    tur.goto(0, 0)
    tur.setheading(90)
    for _ in range(12):
        tur.fd(190)
        tur.pendown()
        tur.fd(20)
        tur.penup()
        tur.goto(0, 0)
        tur.rt(30)

    # Draw the clock hands
    clockhands = [("yellow", 80, 12), ("green", 150, 60), ("white", 110, 60)]
    timeset = (hour, minute, second)
    for hand in clockhands:
        timepart = timeset[clockhands.index(hand)]
        angle = (float(timepart) / hand[2]) * 360
        tur.penup()
        tur.goto(0, 0)
        tur.color(hand[0])
        tur.setheading(90)
        tur.rt(angle)
        tur.pendown()
        tur.fd(hand[1])


# Main loop to update the clock
while True:
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))

    # Clear previous drawing and redraw the clock
    tur.clear()
    draw_clock(hour, minute, second, tur)

    # Update the screen
    ws.update()

    # Sleep for 1 second to update every second
    time.sleep(1)

# Keep the window open (this line will not be reached due to the infinite loop)
# ws.mainloop()
