from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.ht()
        self.goto(0, 0)
        self.st()

    def increase_ball_speed(self):
        speed_increase = 1
        if self.x_move < 0:
            self.x_move -= speed_increase
        else:
            self.x_move += speed_increase
        if self.y_move < 0:
            self.y_move -= speed_increase
        else:
            self.y_move += speed_increase

    def reset_ball_speed(self):
        if self.x_move < 0:
            self.x_move = -10
        else:
            self.x_move = 10
        if self.y_move < 0:
            self.y_move = -10
        else:
            self.y_move = 10
