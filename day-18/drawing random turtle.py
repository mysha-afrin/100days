import turtle as t
from turtle import Screen
import random


tim = t.Turtle()
tim.speed("fastest")
tim.pensize(10)


colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown"]
directions = [0, 90, 180, 270]


for _ in range(200):
    tim.forward(30)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
    

screen = Screen()
screen.exitonclick()