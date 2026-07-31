from turtle import Turtle
starting_position = [(0, 0), (-10, 0), (-20, 0)]
move_distance=10
up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head= self.segment[0]
    def create_snake(self):
        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.turtlesize(0.5)
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)
    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def go_up(self):
        if self.head.heading() != down:  # not already going down
            self.head.setheading(up)

    def go_down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def go_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def go_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.turtlesize(0.5)  # default is 1, so 0.5 = half size
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def grow(self):
        self.add_segment(self.segment[-1].position())