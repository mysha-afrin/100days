
import random
from turtle import Turtle, Screen
import game_essentials
import time
from game_essentials import Player

screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
#player = Player()

l_paddle = game_essentials.l_paddle
r_paddle = game_essentials.r_paddle

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()