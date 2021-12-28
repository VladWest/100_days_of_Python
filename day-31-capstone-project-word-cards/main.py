from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
SMALL_TITLE_FONT = ("Ariel", 32, "italic")
BIG_TITLE_FONT = ("Ariel", 48, "bold")


# ---------------------------- PICKING UP THE WORDS------------------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    data = pandas.read_csv("data/french_words.csv")

data_dic = data.to_dict(orient="records")
current_card = {}


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dic)
    french_word = current_card['French']

    # Changing text in canvas
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_bg_img, image=card_front_img)

    # Will turn on flip card function in 3 seconds
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg_img, image=card_back_img)


def right_click():
    data_dic.remove(current_card)
    print("Right_click")
    next_word()


def wrong_click():
    data = pandas.DataFrame.from_dict(data_dic)
    data.to_csv("data/words_to_learn.csv", index=False, mode="w")
    print("Wrong click")
    next_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Words Cards")
window.config(padx=35, pady=35, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)

# Adding canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# Creating images for cards
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
# Adding images to canvas
card_bg_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=SMALL_TITLE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=BIG_TITLE_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Adding buttons
# wrong button
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=wrong_click)
wrong_button.grid(row=1, column=0)

# right button
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=right_click)
right_button.grid(row=1, column=1, pady=20)

next_word()

window.mainloop()
