from tkinter import *

window = Tk()
window.title("Miles to kilometer converter")
window.minsize(width=350, height=200)
window.config(padx=45, pady=50)

# Entry or input
entry = Entry(width=10, font=("Arial", 14))
entry.grid(row=1, column=1)
# label Miles
miles = Label(text="Miles", font=("Arial", 14))
miles.grid(row=1, column=2)
# label is equal to
is_equal_to = Label(text="is equal to", font=("Arial", 14))
is_equal_to.grid(row=2, column=0)
# Label num_in_km
num_in_km = Label(text="0", font=("Arial", 14))
num_in_km.grid(row=2, column=1)
# label KM
km = Label(text="KM", font=("Arial", 14))
km.grid(row=2, column=2)


def calculate():
    entry_data = int(entry.get())
    result = str(round(entry_data * 1.6))
    num_in_km.config(text=result)

# Calculate button

button = Button(text="Calculate", font=("Arial", 14), command=calculate)
button.grid(row=3, column=1)

window.mainloop()
