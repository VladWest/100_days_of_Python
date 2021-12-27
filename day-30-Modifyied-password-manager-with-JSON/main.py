from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# library used for copying to clipboard
import pyperclip
import json

FONT_NAME = "Courier"
FONT = (FONT_NAME, 13)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for letter in range(randint(8, 10))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]
    password_list += [choice(numbers) for number in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    # copying password to clipboard
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webpage = website_entry.get()
    e_mail_add = e_mail_entry.get()
    passw = password_entry.get()
    new_data = {webpage: {
        "e-mail": e_mail_add,
        "password": passw
    }}

    if len(webpage) < 1 or len(passw) < 1:
        messagebox.showinfo(title="Some info missed", message="Please fill up all fields")
    else:
        try:
            with open("data.json", mode="r") as data_write_file:
                # Reading old data
                data = json.load(data_write_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_write_file:
                # Adding new data to Json file
                json.dump(new_data, data_write_file, indent=4)
        else:
            # Updating old data
            data.update(new_data)
            with open("data.json", mode="w") as data_write_file:
                # Adding new data to Json file
                json.dump(data, data_write_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------------SEARCH MECHANISM----------------------------#
def search_web():
    webpage = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="File does not exist", message="Sorry, but you did not saved any passwords yet")
    else:
        if webpage in data:
            print(data[webpage])
            user_e_mail = data[webpage]["e-mail"]
            password = data[webpage]["password"]
            messagebox.showinfo(title=webpage, message=f"E-mail: {user_e_mail}\n Password: {password}")
        elif len(webpage) < 1:
            messagebox.showwarning(title="Key does not exist!", message="Please, enter webpage name")
        else:
            messagebox.showwarning(title="Key does not exist!", message="The password for this "
                                                                        "webpage have not been created yet")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Adding canvas with logo on the middle of the screen
canvas = Canvas(width=220, height=220, highlightthickness=0)
# reading image from the File system
logo_img = PhotoImage(file="logo.png")
# adding image to canvas
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website label
website = Label(text="Website: ", font=FONT)
website.grid(row=1, column=0)

# Website Entry or input
website_entry = Entry(width=21, font=FONT)
website_entry.focus()
website_entry.grid(row=1, column=1)

# Search button
search = Button(text="Search", font=(FONT_NAME, 12), width=13, command=search_web)
search.grid(row=1, column=2, pady=5)

# E-mail label
e_mail = Label(text="E-mail/Username: ", font=FONT)
e_mail.grid(row=2, column=0)

# E-mail Entry or input
e_mail_entry = Entry(width=35, font=FONT)
e_mail_entry.insert(0, "vlad@gmail.com")
e_mail_entry.grid(row=2, column=1, columnspan=2, pady=5)

# Password label
password_label = Label(text="Password: ", font=FONT)
password_label.grid(row=3, column=0)

# Password Entry or input
password_entry = Entry(width=21, font=FONT)
password_entry.grid(row=3, column=1)

# Password generate button
generate = Button(text="Generate", font=(FONT_NAME, 12), width=13, command=generate_password)
generate.grid(row=3, column=2, pady=5)

# Add password button
add = Button(text="Add", font=(FONT_NAME, 12), width=36, command=save)
add.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
