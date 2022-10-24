import smtplib

# Credentials for mail box
email = ""
passw = ""


# SMTP server should be reviewed since Google does not support smptplib as non secure app
def send_email(my_email, password, message, subject, recipient_email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Row below make connection secure
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject: {subject}\n\n {message}"
        )
