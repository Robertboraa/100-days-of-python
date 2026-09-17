import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

empire_website = response.text
soup = BeautifulSoup(empire_website, "html.parser")
movies = soup.find_all("h3", class_="title")
movie_list = []


for movie in movies:
    name = movie.getText()
    movie_list.append(name)
movie_list.reverse()


with open("output.txt", "w") as f:
    for item in movie_list:
        f.write(str(item) + "\n")





