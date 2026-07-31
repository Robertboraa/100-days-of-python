import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(random.randint(-300, 300), random.randint(-250, 250))

    def move(self, speed):
        self.backward(speed)
        if self.xcor() < -320:
            self.goto(300, random.randint(-250, 250))  # respawn on right