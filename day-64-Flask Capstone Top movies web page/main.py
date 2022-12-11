from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# #CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_KEY_TMDB = "218d5dd8a59b3675cabe304eb49a8e2d"
TMDB_ENDPOINT_SEARCH = f"https://api.themoviedb.org/3/search/movie"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(400))
    img_url = db.Column(db.String(400), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Creating a table
with app.app_context():
    db.create_all()

# Add the first record
# CREATE RECORD
# with app.app_context():
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()


# Form for Updating information about the movie
class MovieEdit(FlaskForm):
    rating = StringField('Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')


# Form for Adding the movie to list
class MovieAdd(FlaskForm):
    title = StringField('Please enter the movie title', validators=[DataRequired()])
    submit = SubmitField('Done')


@app.route("/")
def home():
    # #READ ALL RECORDS
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()
    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    form = MovieEdit()
    movie_id = request.args.get('id')
    if form.validate_on_submit():
        updated_rating = str(form.rating.data)
        updated_review = str(form.review.data)
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = updated_rating
        movie_to_update.review = updated_review
        db.session.commit()
        return redirect(url_for('home'))
    movie_selected = Movie.query.get(movie_id)
    return render_template("edit.html", form=form, movie=movie_selected)


@app.route("/delete", methods=["GET"])
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def add():
    form = MovieAdd()
    if form.validate_on_submit():
        movie_title = str(form.title.data)
        query_params = {
            "api_key": API_KEY_TMDB,
            "query": movie_title
        }
        response = requests.get(TMDB_ENDPOINT_SEARCH, params=query_params)
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/select", methods=["POST", "GET"])
def select():
    movie_id = request.args.get('id')
    query_params = {
        "api_key": API_KEY_TMDB,
    }
    get_movie_details_endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(get_movie_details_endpoint, params=query_params)
    data = response.json()
    year = int(data["release_date"][:4])
    new_movie = Movie(
        title=data["title"],
        year=year,
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)




