from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.goto(0, 280)
        self.penup()
        self.score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        score_text = f"Score: {self.score}"
        self.write(score_text, False, align="center", font=("Arial", 12, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", False, align="center", font=("Arial", 12, "bold"))

