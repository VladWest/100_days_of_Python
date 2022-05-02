from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)

current_year = date.today().year


@app.route('/')
def hello_world():
    random_number = random.randint(0, 10)
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    gender_data = requests.get(f"https://api.genderize.io?name={name}").json()
    gender = gender_data["gender"]
    age_data = requests.get(f"https://api.agify.io?name={name}").json()
    age = age_data["age"]
    national_data = requests.get(f"https://api.nationalize.io?name={name}").json()
    nationality = national_data["country"][0]["country_id"]
    return render_template("guess.html", age=age, name=name, gender=gender, nationality=nationality)


if __name__ == "__main__":
    app.run(debug=True)