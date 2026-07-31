from turtle import Turtle
class Board(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_position)


    def go_up(self):
        if self.ycor() < 255:
            y= self.ycor() + 30
            self.goto(self.xcor(), y)


    def go_down(self):
        if self.ycor() > -255:
            y = self.ycor() - 30
            self.goto(self.xcor(), y)

