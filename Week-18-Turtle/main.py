
import turtle as t
import random
tim = t.Turtle()
tim.speed(3)
t.colormode(255)
"""rgb_colors=[]
# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg.avif', 90)
for color in colors:
    r = color.rgb.r                                            Extracting the right format of colors
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))
print(rgb_colors)"""
tim.hideturtle()
color_list =[(203, 171, 107), (221, 227, 234), (152, 181, 196), (193, 161, 176), (151, 187, 174), (214, 204, 111), (207, 179, 198), (163, 202, 214), (174, 189, 213), (159, 214, 188), (113, 123, 186), (215, 180, 180), (181, 160, 66), (200, 206, 44), (101, 113, 153)]
def hrists_painter(surface_area):
    tim.teleport(-300, 300)
    y = tim.ycor()
    x = tim.xcor()
    tim.penup()
    for i in range(surface_area):
        tim.goto(x,y)
        for i in range(surface_area):
            tim.dot(20)
            tim.color(random.choice(color_list))
            tim.forward(50)
        y -= 50




hrists_painter(10)

hrists_painter()
screen = t.Screen()
screen.exitonclick()