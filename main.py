from Reservatiesysteem import Reservatiesysteem
from movieApi import getMovies

def main():
    reservatieSysteem = Reservatiesysteem()

    names, ratings = getMovies()
    for name, rating in zip(names, ratings):
        reservatieSysteem.addMovie(name, rating)
    reservatieSysteem.movies.inorderTraverse(print)

if __name__ == "__main__":
    main()