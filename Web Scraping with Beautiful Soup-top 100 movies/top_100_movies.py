from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
movie_titles = soup.select(selector=".article-title-description .article-title-description__text h3")

for i in movie_titles[::-1]:
    movies = i.getText()
    with open("movies.txt", "a", encoding="utf8") as file:
        contents = file.write(movies + "\n")



