#File: exercise_16.py
#Description: using loops to draw squres within each other
#Assignment Number: chapter4-16
#Kevin Liu
#Github<barbqueen>

import turtle

turtle.speed(30)
l = 5

for x in range(100):
    for y in range(4):
        turtle.forward(l)
        turtle.left(90)
    l += 5

turtle.exitonclick()
