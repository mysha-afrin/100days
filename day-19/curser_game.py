from turtle import Turtle, Screen

tim = Turtle()
def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_clockwise():
    tim.setheading(tim.heading() - 10)
def turn_left():
    tim.heading(10) 
def turn_right():
    tim.right(10)
def draw_circle():
    tim.circle(10)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "l", fun = turn_left)
screen.onkey(key = "r", fun = turn_right)
screen.onkey(key = "c", fun = draw_circle)
screen.onkey(key = "e", fun = clear_drawing)

screen.exitonclick()