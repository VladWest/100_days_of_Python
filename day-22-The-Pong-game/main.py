from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game.")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

the_game_is_on = True

while the_game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 325) or (ball.distance(l_paddle) < 50 and ball.xcor() < -325):
        ball.increase_ball_speed()
        ball.bounce_x()


    # Right paddle misses
    if ball.xcor() > 400:
        ball.reset_ball_speed()
        ball.reset_ball()
        ball.x_move *= -1
        score.add_l_score()


    # Left paddle misses
    if ball.xcor() < -400:
        ball.reset_ball_speed()
        ball.reset_ball()
        ball.x_move *= -1
        score.add_r_score()



screen.exitonclick()
