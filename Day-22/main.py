from turtle import Screen
from boards import Board
from ball import Ball
from scoreboard import Scoreboard
import time
ball = Ball()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

left_board = Board((-350,0))
right_board = Board((350,0))


screen.listen()
# left board: W / S keys
screen.onkeypress(fun=left_board.go_up, key="w")
screen.onkeypress(fun=left_board.go_down, key="s")
# right board: Up / Down keys
screen.onkeypress(fun=right_board.go_up, key="Up")
screen.onkeypress(fun=right_board.go_down, key="Down")
""
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    # bounce off top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # bounce off left board
    if ball.distance(left_board) < 40:
        ball.bounce_x()

    # bounce off right board
    if ball.distance(right_board) < 40:
        ball.bounce_x()
    # ball goes out — award point and reset
    if ball.xcor() > 320:
        scoreboard.left_point()  # right side missed, left gets point
        ball.goto(0, 0)
        ball.bounce_x()

    if ball.xcor() < -320:
        scoreboard.right_point()  # left side missed, right gets point
        ball.goto(0, 0)
        ball.bounce_x()



screen.exitonclick()