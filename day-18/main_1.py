import turtle as t
from turtle import Screen, colormode 
import random
tim = t.Turtle()
tim.pensize(5)
#colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for num_sides in range(3, 10):
    angle = 360 / num_sides
    for _ in range(num_sides):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        tim.forward(100)
        tim.right(angle)
        

screen = Screen()
screen.exitonclick()
screen.colormode(255)