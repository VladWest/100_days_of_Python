from flask import Flask
app = Flask(__name__)

print(__name__)


def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper


def make_em(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper


@app.route('/')
@make_bold
@make_em
def hello_world():
    return 'Hello, World!'


# Passing variable to the route and creating greeting by user input
@app.route('/username/<name>')
def greet(name):
    return f'Hello, {name}!'


if __name__ == "__main__":
    app.run(debug=True)

