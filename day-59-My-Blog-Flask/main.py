from flask import Flask, render_template, url_for, request
import requests
from datetime import date
# Importing all needed functions from file in project
from mail import send_email, email, passw

app = Flask(__name__)

# Name of the all web-page
site_name = "MyOwnBlog"
# Getting data from the  npoint.io which are nice web service and could be used for creation json files
# Here this service used as database for posts
# This json file also contain links to the images which were hosted on the https://imgbb.com/?  - free image hosting
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


# Route which will render the page for one particular posts which was chosen by user on a main page
@app.route('/posts/<p_id>')
def show_post(p_id):
    post_id = int(p_id)
    return render_template("one_post.html", post_id=post_id, posts=all_posts)


# These variables contain text for default title and subtitle on the contact page
contact_page_title = "Contact Me"
contact_page_subtitle = "Have questions? I have answers."


@app.route('/contact')
def contact_page():
    current_year = date.today().year
    return render_template("contact.html", site_name=site_name, year=current_year,
                           title=contact_page_title, subtitle=contact_page_subtitle)


# route to the page which should proceed request
@app.route('/form-entry', methods=['GET', 'POST'])
def get_data():
    # Getting date from the request create a dictionary and checking if dictionary is not empty
    data = request.form.to_dict()
    current_year = date.today().year
    if request.method == 'POST' and len(data) > 0:

        # Below you can find code which send data from the form to email and will show success
        # text in the contact page banner in case if email will be sent
        # The code has been commented because Google stop supporting smptplib as a non-secure app

        # Creating all needed for email sending variables
        # send_to = ""
        # subject = "Email from your blog"
        # msg = f"Name: {request.form['name']}, Phone: {request.form['phone']}, " \
        #       f"Email: {request.form['email']}, message: {request.form['message']}"
        # Sending an email
        # Check if email func return true, mean that email has been send, if not will be rendered contact page with
        # error message
        # if send_email(my_email=email, password=passw, message=msg, subject=subject, recipient_email=send_to):
        #     # rendering the page with dedicated success message as a big title
        #     success_title = "Successfully sent message"
        #     success_subtitle = f""
        #     return render_template("contact.html", site_name=site_name, year=current_year,
        #                            title=success_title, subtitle=success_subtitle)
        # else:
        #     title = "Something went wrong!"
        #     subtitle = "Your message has not been sent, please try one more time"
        #     return render_template("contact.html", site_name=site_name, year=current_year,
        #                            title=title, subtitle=subtitle)

        success_title = "Successfully sent message"
        success_subtitle = f""
        return render_template("contact.html", site_name=site_name, year=current_year,
                               title=success_title, subtitle=success_subtitle)
    elif request.method == 'POST' and len(data) <= 0:
        title = "Something went wrong!"
        subtitle = "Your message has not been sent, please try one more time"
        return render_template("contact.html", site_name=site_name, year=current_year,
                               title=title, subtitle=subtitle)
    elif request.method == 'GET':
        return render_template("contact.html", site_name=site_name, year=current_year,
                               title=contact_page_title, subtitle=contact_page_subtitle)


if __name__ == "__main__":
    app.run(debug=True)

