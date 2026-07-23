import turtle as t
import random
tim = t.Turtle()
directions = [0, 90, 180, 270]
tim.pensize(1)
tim.speed(0)
t.colormode(255)
def random_color_tuple():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.pencolor(random_color_tuple())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(10)

















screen = t.Screen()
screen.exitonclick()