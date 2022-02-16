from bs4 import BeautifulSoup
import requests

# Getting data from  ycombinatpr web page
response = requests.get("https://news.ycombinator.com/")
y_comb_page = response.text

# Making soup from response
soup = BeautifulSoup(y_comb_page, "html.parser")

# Finding all articles on a page
articles = soup.find_all(class_="titlelink")
article_texts = []
article_links = []

# Taking articles texts and links and adding them to a list
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

# Creating list with articles points (only with integer numbers)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Printing results
print(article_upvotes)
print(article_texts)
print(article_links)

# Looking for article which have max points, all lists have same indexes
# Means that index of biggest points item in points list = to index of article and index of link
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])

