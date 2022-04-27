from flask import Flask
from random import randint

app = Flask(__name__)
guess = randint(0, 10)
print(guess)


@app.route('/')
def hello_world():
    return '<h1>Hey! Guess number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:variable>')
def guess_func(variable):
    if variable < guess:
        return f'<h1 style="color:red">{variable} is too low!</h1>' \
               f'<img src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif variable > guess:
        return f'<h1 style="color: blue"> {variable} is too High, try again!</h1>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif variable == guess:
        return f'<h1>You found me!</h1>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    else:
        return 'Looks like something went wrong'


if __name__ == "__main__":
    app.run(debug=True)
