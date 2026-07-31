from turtle import Screen
import random
import time
from car import Car
from in_game_turtle import InGameTurtle
from leveltracker import LevelTracker

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Cross the road")
screen.tracer(0)

in_game_turtle = InGameTurtle()
level_tracker = LevelTracker()
cars = [Car() for _ in range(10)]
car_speed = 5

screen.listen()
screen.onkey(fun=in_game_turtle.move, key="Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move(car_speed)

    # level up when turtle reaches top
    if in_game_turtle.ycor() > 280:
        in_game_turtle.reset_turtle()
        car_speed += 5
        level_tracker.increase_score()

    # collision detection
    for car in cars:
        if in_game_turtle.distance(car) < 20:
            level_tracker.game_over()
            game_on = False

screen.exitonclick()