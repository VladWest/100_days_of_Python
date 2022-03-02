import requests
from bs4 import BeautifulSoup
import lxml
import pprint
import smtplib

# Credentials for mail box
my_email = "stepafarm1101@gmail.com"
password = "A232D83M_in905!"

URL = "https://www.amazon.com/ASUS-Graphics-DisplayPort-Military-Grade-Certification/dp/B096YPLGHG/ref=sr_1_19?crid=2AZOHPFN0QEUQ&keywords=GPU&qid=1646213659&sprefix=gpu%2Caps%2C177&sr=8-19"
headers = {
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8,uk;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

response = requests.get(url=URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "lxml")
title = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break")
price_string = soup.find(name="span", class_="a-offscreen").getText()

product_name = title.getText().lstrip().rstrip()
print(product_name)
price0 = price_string.split('$')[1]
price1 = float(price0.split(',')[0]) + 999
total_price = float(price0.split(',')[1]) + price1
print(total_price)

message = f"""
Hey Vlad,
You can find the {product_name}.
By link {URL}.
The price now is {total_price}
"""

# message = f"New price for {product_name}, is {total_price}. Check link {URL}"

#  Send the letter generated in step 3 to that person's email address.
# Please, pay additional attention to the port configuration

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # Row below make connection secure
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="vladsv001@gmail.com",
        msg=f"Subject: Good price on GPU\n\n {message}"
    )
