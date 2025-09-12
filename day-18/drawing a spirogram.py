import turtle as t 
from turtle import Screen, Turtle
import random
screen = Screen()
screen.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.pensize(2)

for _ in range(100):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)
    tim.circle(100)
    tim.setheading(tim.heading() + 10)

screen.exitonclick()