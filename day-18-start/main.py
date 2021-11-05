from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("black", "OliveDrab3")
turtle.speed(1)
turtle.shapesize(2, 2, 3)
turtle.penup()
turtle.setpos(0, 300)
turtle.pendown()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    turtle.pencolor(R, G, B)


lines = 3

while lines <= 10:
    angle = 360 / lines
    for _ in range(lines):
        turtle.forward(100)
        turtle.right(angle)
    lines += 1
    change_color()


screen = Screen()
screen.exitonclick()