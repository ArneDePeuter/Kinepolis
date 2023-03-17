from Kinepolis import Kinepolis
#from movieWebScraper import getMovies

def main():
    kinepolis = Kinepolis()
    kinepolis.load("system.txt")
    #kinepolis.save("Tests/Output/output.html")

    """
    webscraper
    names, ratings = getMovies()
    for name, rating in zip(names, ratings):
        reservatieSysteem.addMovie(name, rating)
    reservatieSysteem.movies.inorderTraverse(print)
    """

if __name__ == "__main__":
    main()