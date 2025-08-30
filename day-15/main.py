from turtle import Turtle
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.shape("turtle")
timmy.color("aquamarine4")
timmy.forward(100)#move the turtle forward by 100 units
my_screen = timmy.getscreen()
print(my_screen.canvheight)
my_screen.exitonclick() #this line keeps the screen open untill we click on it.

