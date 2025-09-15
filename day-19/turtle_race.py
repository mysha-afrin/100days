from turtle import Turtle, Screen
import random

tim = Turtle()
timmy = Turtle()
tommy = Turtle()
teddy = Turtle()
tina = Turtle()
toby = Turtle()

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
tim.color(random.choice(colors))
timmy.color(random.choice(colors))
tommy.color(random.choice(colors))
teddy.color(random.choice(colors))
tina.color(random.choice(colors))
toby.color(random.choice(colors))


tim.shape("turtle")
timmy.shape("turtle")
tommy.shape("turtle")
teddy.shape("turtle")
tina.shape("turtle")
toby.shape("turtle")








screen = Screen()

screen.exitonclick()