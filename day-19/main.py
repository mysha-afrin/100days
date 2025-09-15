from turtle import Turtle, Screen

tim = Turtle()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)


screen = Screen()
screen.listen()
screen.onkey(key = "space", fun = move_forwards)
screen.onkey(key = "b", fun = move_backwards)
screen.exitonclick()