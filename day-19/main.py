from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which color will win?")
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
y_cordinates = [100 ,80,60,40,20,0]
all_turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-200 ,y_cordinates[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet :
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            print(f"{turtle.pencolor()} Turtle wins!")
            if turtle.pencolor() == user_bet :
                print("You win!")
            else:
                print("You lose!")
            race_is_on = False

        rand_distance=random.randint(1,10)
        turtle.forward(rand_distance)


screen.exitonclick()

