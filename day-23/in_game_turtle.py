from turtle import Turtle
class InGameTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.goto(0,-280)
        self.setheading(90)
    def move(self):
        self.forward(10)
    def reset_turtle(self):
        self.goto(0,-280)