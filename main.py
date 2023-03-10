from Reservatiesysteem import Reservatiesysteem
#from movieWebScraper import getMovies

def main():
    reservatieSysteem = Reservatiesysteem()
    reservatieSysteem.load("Tests/Input/system.txt")
    reservatieSysteem.save("Tests/Output/output.html")


    """
    webscraper
    names, ratings = getMovies()
    for name, rating in zip(names, ratings):
        reservatieSysteem.addMovie(name, rating)
    reservatieSysteem.movies.inorderTraverse(print)
    """




if __name__ == "__main__":
    main()