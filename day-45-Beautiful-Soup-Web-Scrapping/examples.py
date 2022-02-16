from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# We can looking by tag name
# print(soup.title)

# Also we can look by tag content
# print(soup.title.string)

# Here we can looking for something special
# In example below we are checking for all a tags and adding them to a list
an_anchor_tags = soup.findAll(name="a")
print(an_anchor_tags)

# Below you can find the way of getting all content from tags
# for tag in an_anchor_tags:
#     print(tag.getText())

# Below you can find example how to get all needed link from a tag
for link in soup.findAll("a"):
    print(link.get("href"))

# Below you can see how to find element if you need element with special id or class
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# Also we are able to do select element except of finding

name = soup.select_one(selector="#name")
print(name)
# Using method below we will get a list with elements
headings = soup.select(selector=".heading")
print(headings)

