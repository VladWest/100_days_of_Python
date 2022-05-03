from flask import Flask, render_template
import requests


app = Flask(__name__)

all_posts = requests.get('https://api.npoint.io/aa8e15eedbcec2582e41').json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/posts/<p_id>')
def show_post(p_id):
    post_id = int(p_id)
    return render_template("post.html", post_id=post_id, posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
