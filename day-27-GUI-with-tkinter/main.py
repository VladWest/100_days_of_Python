import tkinter

window = tkinter.Tk()
window.title("My first GUI with Tkinter")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

# Creating a label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 14, "bold"))
# To show up label we need to use function below
# pack method allow us to place the widgets only using some kind of sides
# my_label.pack()
# For the placing we are able to use coordinates also
# For using coordinates we should use .place() method and arguments x and y like on the exmple below
# my_label.place(x=0, y=0)

# But the easiest way to placed widgets on the screen is to use .grid()  method
my_label.grid(column=0, row=0)
my_label.config(padx=35, pady=30)

# Ways how we can change the config
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


def button_clicked():
    # my_label.config(text="You just clicked the button")
    text_from_input = input_comp.get()
    my_label.config(text=text_from_input)


# creation the button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)
# button.pack()
# creation the button
button2 = tkinter.Button(text="New_button", command=button_clicked)
button2.grid(row=0, column=2)
# Entry component = input

input_comp = tkinter.Entry(width=10)
input_comp.grid(row=2, column=3)
# input_comp.pack()



window.mainloop()
