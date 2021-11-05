from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

if_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -65, -30, 5, 40, 75]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    if_race_on = True

while if_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle win.")
            else:
                print(f"You've lost! The {winning_color} turtle was first!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
