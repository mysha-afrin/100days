import turtle as t
from turtle import Screen
import random
tim = t.Turtle()
for _ in range(6):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.right(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()