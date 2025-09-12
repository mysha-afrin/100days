import turtle as t
from turtle import Screen
import random

screen = Screen()
screen.colormode(255)

tim = t.Turtle()
#colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


tim.pensize(15)
tim.speed("fastest")

directions = [0, 90, 180, 270]

for _ in range(200):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)
    tim.forward(30)
    tim.setheading(random.choice(directions))
    


screen.exitonclick()

#tim --- IGNORE ---