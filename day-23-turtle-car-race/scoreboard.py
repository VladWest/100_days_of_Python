from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.ht()
        self.start_level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.start_level}", align="left", font=FONT)

    def increase_score(self):
        self.start_level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=FONT)
