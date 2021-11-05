import turtle as t
from turtle import Screen
import random

t.colormode(255)
tim = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


directions = [0, 90, 180, 270]
tim.shape("arrow")
tim.speed("fastest")


def draw_spirograph(step):
    angle = 0
    while angle <= 360:
        tim.setheading(angle)
        tim.color(random_color())
        tim.circle(100)
        angle += step

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


draw_spirograph(1)

screen = Screen()
screen.exitonclick()
