from Reservatiesysteem import Reservatiesysteem
from movieWebScraper import getMovies

def main():
    reservatieSysteem = Reservatiesysteem()

    names, ratings = getMovies()
    for name, rating in zip(names, ratings):
        reservatieSysteem.addMovie(name, rating)
    reservatieSysteem.movies.inorderTraverse(print)
    print(reservatieSysteem.movies.save())

    

if __name__ == "__main__":
    main()