# ___________________ Extra Hard Starting Project__________________________
import smtplib
import datetime as dt
import random
import pandas

# Credentials for mail box
my_email = ""
password = ""

# 1. Update the birthdays.csv, pick up data from csv file

# Picking up current date
now = dt.datetime.now()
current_month = now.month
current_day = now.day

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
today_b_days = []

for (index, row) in data.iterrows():

    if row["day"] == current_day and row["month"] == current_month:
        today_b_person = {
            "Name": row["name"],
            "email": row["email"]
        }
        today_b_days.append(today_b_person)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
if len(today_b_days) > 0:
    for person in today_b_days:
        letter_num = random.randint(1, 3)
        letter_data = open(f"letter_templates/letter_{letter_num}.txt")
        letter_message = letter_data.read()
        letter_data.close()
        message = letter_message.replace("[NAME]", person["Name"])
        recipient_email = person["email"]
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Row below make connection secure
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient_email,
                msg=f"Subject: Happy birthday!\n\n {message}"
            )
