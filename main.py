from Reservatiesysteem import Reservatiesysteem
#from movieWebScraper import getMovies

def main():
    reservatieSysteem = Reservatiesysteem()
    print("Hello main")
    reservatieSysteem.readFile("Tests/Input/system.txt")
    """names, ratings = getMovies()
    for name, rating in zip(names, ratings):
        reservatieSysteem.addMovie(name, rating)
    reservatieSysteem.movies.inorderTraverse(print)"""




if __name__ == "__main__":
    main()