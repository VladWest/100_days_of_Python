from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv
import requests
# Import writer class from csv module
from csv import writer

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location URL to Google Maps', validators=[DataRequired()])
    cafe_open_time = StringField('Cafe opening at...', validators=[DataRequired()])
    cafe_close_time = StringField('Cafe closed at...', validators=[DataRequired()])
    cafe_coffee_rating = SelectField('PLease set up coffee rating',
                                     choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                                     validators=[DataRequired()])
    cafe_wifi_rating = SelectField('PLease set up wifi rating',
                                   choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                                   validators=[DataRequired()])
    cafe_power_supply_rating = SelectField('PLease set up power supply rating',
                                           choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                                           validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


# Exercise:
# Make the form write a new row into cafe-data.csv
# with   if form.validate_on_submit()
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        list_row = []
        name = str(form.cafe.data)
        location = str(form.cafe_location.data)
        open_time = str(form.cafe_open_time.data)
        close = str(form.cafe_close_time.data)
        coffee = str(form.cafe_coffee_rating.data)
        wifi = str(form.cafe_wifi_rating.data)
        power_spl = str(form.cafe_power_supply_rating.data)
        # List that we want to add as a new row
        list_row.extend([name, location, open_time, close, coffee, wifi, power_spl])
        new_line = ", ".join(list_row)

        # Open our existing CSV file in append mode
        csv_file = open("cafe-data.csv", mode="a", newline='', encoding="utf-8")
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(csv_file, delimiter=',')
        # Pass the list as an argument into`
        # the writerow()
        writer_object.writerow(list_row)
        # Close the file object
        # csv_file.writerow(new_line)
        csv_file.close()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    # with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
    #     csv_data = csv.reader(csv_file, delimiter=',')
    #     list_of_rows = []
    #     for row in csv_data:
    #         list_of_rows.append(row)
    #     csv_file.close()
    csv_file = open('cafe-data.csv', newline='', encoding='utf-8')
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)
    csv_file.close()

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
