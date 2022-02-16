from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "html.parser")
movies_data = soup.find_all(name="h3", class_="title")
movies = []
for movie in movies_data:
    title = movie.getText()
    movies.append(title)

movies.reverse()

out_data = open("list_of_movies.txt", mode="w", encoding="utf-8")
for movie in movies:
    out_data.write(movie)
    out_data.write("\n")
out_data.close()



