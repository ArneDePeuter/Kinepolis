from Reservatiesysteem import Reservatiesysteem
#from movieWebScraper import getMovies
from Tests.Parser import readFile

def main():
    reservatieSysteem = Reservatiesysteem()
    readFile(reservatieSysteem, "Tests/Input/system.txt")
    print("Hello main")
    """names, ratings = getMovies()
    for name, rating in zip(names, ratings):
        reservatieSysteem.addMovie(name, rating)
    reservatieSysteem.movies.inorderTraverse(print)"""




if __name__ == "__main__":
    main()