from turtle import Turtle
class LevelTracker(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.update_score()
        self.color("white")

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.level += 1
        self.update_score()
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 18, "normal"))