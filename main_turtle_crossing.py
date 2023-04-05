import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

CAR_AMOUNT = 25

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(fun=player.move, key="Up")

cars = []
for car in range(CAR_AMOUNT):
    new_car = CarManager()
    cars.append(new_car)

for _ in range(3):
    for car in range(len(cars)):
        for other_car in range(car + 1, len(cars)):
            if abs(cars[car].xcor() - cars[other_car].xcor()) < 60 and abs(cars[car].ycor() - cars[other_car].ycor()) < 60:
                cars[car].refresh()



game_is_on = True
while game_is_on:
    time.sleep(0.1) #defining a lag before each screen update
    screen.update()

    for car in range(len(cars)):
        for other_car in range(car + 1, len(cars)):
            if cars[car].xcor() > 280 and cars[other_car].xcor() > 295 and abs(cars[car].xcor() - cars[other_car].xcor()) < 60 and abs(cars[car].ycor() - cars[other_car].ycor()) < 60:
                cars[car].go_back()

    for car in cars:
        if abs(player.xcor() - car.xcor()) < 30 and abs(player.ycor() - car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False

    #detecting arrival to upper bound: actions
    if player.ycor() > 280:
        #bring player back to starting position
        player.level_up()
        cars[0].level_up()



        #Adding score
        scoreboard.level_up()

        #Increasing car speed
        # car_manager.level_up()

    #controlling each of the cars
    for car in cars:
        car.move()
        if car.xcor() < -280:
            car.go_back()



screen.exitonclick()

