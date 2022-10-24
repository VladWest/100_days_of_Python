from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def get_data():
    data = request.form.to_dict()
    string = f"<h1>Username is {data['username']}, password is {data['password']}"
    return string


if __name__ == "__main__":
    app.run(debug=True)

