
import random
from turtle import Turtle, Screen
import game_essentials
import time
from game_essentials import Player
from ball import Ball


screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
#player = Player()

l_paddle = game_essentials.l_paddle
r_paddle = game_essentials.r_paddle
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    



    

screen.mainloop()