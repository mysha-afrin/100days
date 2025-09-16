from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color:")
y_position = [-70, -40, -10, 20, 50, 80]
tim = Turtle()
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
for turtle_index in range(0, 6):
    tim = Turtle(shape = "turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x = -200, y = y_position[turtle_index])
    
if user_bet:
    is_race_on = True

while is_race_on:
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)



#colors = ["red", "blue", "green", "yellow", "purple", "orange"]
#tim.color(random.choice(colors))












screen.exitonclick()