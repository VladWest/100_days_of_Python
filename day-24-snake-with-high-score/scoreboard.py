from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.update_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        file = open("data.txt", mode="r")
        score_from_file = file.read()
        if int(score_from_file) > int(self.high_score):
            self.high_score = score_from_file
            file.close()
        else:
            file = open("data.txt", mode="w")
            file.write(str(self.high_score))
            file.close()

    def reset(self):
        if int(self.high_score) < self.score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
