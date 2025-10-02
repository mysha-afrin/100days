from turtle import Screen
from player import Player
import time
from car_manager import CarManager

screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
#screen.onkey(player.go_down, "Down")
game_is_on = True
while game_is_on :
    time.sleep(.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    #Detect car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False


screen.exitonclick()