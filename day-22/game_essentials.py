import turtle
from turtle import Turtle

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed("fastest")
    def go_up(self):
        new_y = self.ycor() + 30

        if new_y > 250:
            new_y = 250
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 30
        if new_y < -250:
            new_y = -250
        self.goto(self.xcor(), new_y)
l_paddle = Player((-350, 0))
r_paddle = Player((350, 0))
