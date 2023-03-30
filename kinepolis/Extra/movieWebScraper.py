import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"


def getMovieNames(soup):
    movies = soup.select("td.titleColumn")
    l = []

    for movie in movies:
        movie_spit = movie.text.split()
        name = ""
        for i, text in enumerate(movie_spit):
            if i == 0:
                num = text
            elif i == len(movie_spit) - 1:
                year = text
            else:
                name += text
                if i < len(movie_spit) - 2:
                    name += " "
        l.append(name)
    return l


def getRatings(soup):
    ratings = soup.select("td.ratingColumn.imdbRating")
    l = []
    for rating in ratings:
        l.append(round(float(rating.text.split()[0])/10,2))
    return l


def getMovies():
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")

    return getMovieNames(soup), getRatings(soup)
