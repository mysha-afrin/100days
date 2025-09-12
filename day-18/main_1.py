import turtle as t
from turtle import Screen
import random
tim = t.Turtle()

for num_sides in range(3, 10):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()