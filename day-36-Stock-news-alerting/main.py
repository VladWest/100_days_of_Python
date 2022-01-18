import requests
from datetime import datetime
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_ENDPOINT_API_KEY = "your_key"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "your_news_key"

my_email = ""
password = ""

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_ENDPOINT_API_KEY
}
stock_price_response = requests.get(STOCK_ENDPOINT, params=stock_params)
# Creating an exception in case is API will not provide response
stock_price_response.raise_for_status()
stock_price_data = stock_price_response.json()

current_year = datetime.now().year
current_month = datetime.now().month
if current_month < 10:
    current_month = f"0{current_month}"
current_day = datetime.now().day
if datetime.today().weekday() == 0:
    current_day -= 3
    yesterday = f"{current_year}-{current_month}-{current_day}"
    before_yesterday = f"{current_year}-{current_month}-{current_day - 1}"
elif datetime.today().weekday() == 1:
    current_day -= 4
    yesterday = f"{current_year}-{current_month}-{current_day}"
    before_yesterday = f"{current_year}-{current_month}-{current_day - 1}"
else:
    yesterday = f"{current_year}-{current_month}-{current_day - 1}"
    before_yesterday = f"{current_year}-{current_month}-{current_day - 2}"
# Get yesterday's closing stock price.
# Hint: You can perform list comprehensions on Python dictionaries. e.g.
# [new_value for (key, value) in dictionary.items()]
yesterday_stock_price = float(stock_price_data["Time Series (Daily)"][yesterday]["4. close"])
# print(yesterday_stock_price)
# Get the day before yesterday's closing stock price

before_yesterday_stock_price = float(stock_price_data["Time Series (Daily)"][before_yesterday]["4. close"])
# print(before_yesterday_stock_price)
# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference = abs(yesterday_stock_price - before_yesterday_stock_price)
# Work out the percentage difference in price between closing price yesterday and
# closing price the day before yesterday.
percent_difference = round(100 * difference/before_yesterday_stock_price, 2)
stock_status = "Stocks stable."
if yesterday_stock_price > before_yesterday_stock_price:
    stocks_status = f"Stocks goes up. Difference is:+{percent_difference}%"
elif yesterday_stock_price < before_yesterday_stock_price:
    stocks_status = f"Stocks goes down. Difference is:-{percent_difference}%"

if percent_difference >=1:
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        "q": COMPANY_NAME,
        "from": before_yesterday,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    # Creating an exception in case is API will not provide response
    news_response.raise_for_status()
    news_data = news_response.json()
    news_articles = news_data['articles']
    articles = []
    # Create a new list of the first 3 article's headline and description.
    for i in range(0, 3):
        article = {
            "title": news_articles[i]["title"],
            "description": news_articles[i]["description"]
        }
        articles.append(article)

    # Send each article as a separate message via SMTP.
    article_1 = f"Headline: {articles[0]['title'].encode('utf-8')}\nDescription: {articles[0]['description'].encode('utf-8')}"
    article_2 = f"Headline:{articles[1]['title'].encode('utf-8')} \nDescription: {articles[1]['description'].encode('utf-8')}"
    article_3 = f"Headline: {articles[2]['title'].encode('utf-8')}\nDescription: {articles[2]['description'].encode('utf-8')}"
    message = f"Subject: {COMPANY_NAME} stocks {stocks_status} \n\n {article_1}\n {article_2}\n{article_3}"
    # print(article_1)
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



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


