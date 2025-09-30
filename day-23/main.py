from turtle import Screen
from player import Player
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.tracer()

player = Player()

game_is_on = True
while game_is_on :
    time.sleep(.1)
    screen.update()