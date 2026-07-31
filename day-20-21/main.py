from turtle import Screen
import time
import random
from food import Food
from scorebord import Scoreboard
from snake import Snake
random_y=random.randrange(-280,280)
random_x=random.randrange(-280,280)
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake= Snake()
food=Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=snake.go_up, key="Up")
screen.onkey(fun=snake.go_down, key="Down")
screen.onkey(fun=snake.go_left, key="Left")
screen.onkey(fun=snake.go_right, key="Right")
game_on = True
while game_on:
    screen.update()
    score = scoreboard.score
    level = scoreboard.score // 5
    speed = max(0.05, 0.08 - (level * 0.01))
    time.sleep(speed)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.game_over()
        game_on = False

    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 5:
            scoreboard.game_over()
            game_on = False




















screen.exitonclick()