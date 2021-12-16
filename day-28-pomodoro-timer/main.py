from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    top_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps *= 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps == 8:
        count_down(4)
        # count_down(LONG_BREAK_MIN * 60)
        top_label.config(text="Long brake", fg=RED)
    elif reps % 2 == 0:
        count_down(3)
        # count_down(SHORT_BREAK_MIN * 60)
        top_label.config(text="Short Brake", fg=PINK)
    else:
        count_down(5)
        # count_down(WORK_MIN * 60)
        top_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min == 0 or count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# label on the top
top_label = Label(text="Timer", font=(FONT_NAME, 28), bg=YELLOW, fg=GREEN)
top_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# the way of reading files for tkinter below
tomato_img = PhotoImage(file="tomato.png")
# adding image to canvas
canvas.create_image(103, 112, image=tomato_img)
# adding text to canvas
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

# Start button
start_button = Button(text="Start", font=(FONT_NAME, 14), command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 14), command=reset)
reset_button.grid(row=2, column=2)

# check mark label
check_mark = Label(font=(FONT_NAME, 14, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(row=3, column=1)

window.mainloop()

