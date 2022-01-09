import smtplib
import datetime as dt
import random

my_email = ""
password = ""

with open("quotes.txt", mode="r") as data:
    content = data.read()
    content_list = content.split("\n")

# Working with datetime library
now = dt.datetime.now()
current_day_of_week = now.weekday()
print(current_day_of_week)

if current_day_of_week == 2:
    random_quote = random.choice(content_list)
    message = f"Subject: A bit of motivation for today \n\n {random_quote}"
    # Automtic closure connection
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Row below make connection secure
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="vladsv001@gmail.com",
            msg=message
        )


