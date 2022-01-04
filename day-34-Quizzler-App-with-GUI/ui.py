from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 12)
Q_FONT = ("Arial", 14, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0")
        self.score.config(font=FONT, bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Here you will find a question.",
            fill=THEME_COLOR,
            font=Q_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.true_answer)
        self.true_btn.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.false_answer)
        self.false_btn.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            last_msg = f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_text, text=last_msg)
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
