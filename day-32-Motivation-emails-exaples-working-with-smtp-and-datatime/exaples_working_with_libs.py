import smtplib
import datetime as dt

my_email = "stepafarm1101@gmail.com"
password = "A232D83M_in905!"

# Working with datetime library
now = dt.datetime.now()
# print(now)
year = now.year
month = now.month
current_day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1997, month=1, day=11)
# print(date_of_birth)

# Usual way of sending e-mails
# connection = smtplib.SMTP("smtp.gmail.com")
# Row below make connection secure
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="vladsv001@gmail.com",
#     msg="Subject: Test message \n\nHello, test"
# )
# connection.close()

# Automtic closure connection
with smtplib.SMTP("smtp.gmail.com") as connection:
    # Row below make connection secure
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="vladsv001@gmail.com",
        msg="Subject: Test message \n\nHello, test"
    )
