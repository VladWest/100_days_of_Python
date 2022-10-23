from flask import Flask, render_template, url_for
import requests
from datetime import date

app = Flask(__name__)

site_name = "MyOwnBlog"
all_posts = requests.get('https://api.npoint.io/9bba536aa7959642ecb3').json()


@app.route('/')
def main_page():
    current_year = date.today().year
    return render_template("index.html", site_name=site_name, year=current_year, posts=all_posts)


@app.route('/about')
def about_page():
    current_year = date.today().year
    return render_template("about.html", site_name=site_name, year=current_year)


@app.route('/post')
def post_page():
    current_year = date.today().year
    return render_template("post.html", site_name=site_name, year=current_year)


@app.route('/posts/<p_id>')
def show_post(p_id):
    post_id = int(p_id)
    return render_template("one_post.html", post_id=post_id, posts=all_posts)


@app.route('/contact')
def contact_page():
    current_year = date.today().year
    return render_template("contact.html", site_name=site_name, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)

