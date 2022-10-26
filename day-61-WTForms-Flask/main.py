from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email
# Connecting Flusk Bootstrap
from flask_bootstrap import Bootstrap
import email_validator


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[validators.Length(min=6, max=120), Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[validators.Length(min=6, max=120), DataRequired()])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
# To start working with Flask bootstrap
# All docs is here https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


# Login page with form created with Bootstrap login form
# Different way for form generating including bootstrap styles
@app.route("/login2")
def login2():
    login_form = LoginForm()
    return render_template('login2.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
