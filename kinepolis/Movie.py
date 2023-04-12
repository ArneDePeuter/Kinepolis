from .Factories import ADTFactory
from .MaterializedIndex import MaterializedIndex
from .Extra.movieWebScraper import getMovies


# ADT system that handles everything to do with movies
class MovieSystem:
    def __init__(self) -> None:
        """
        Initializes movieSystem

        preconditions: /
        postconditions: a MovieSystem object is created
        """
        self.datastruct = ADTFactory.getADT("Movie")
        self.count = 0
        self.queries = {}

    def traverse(self, func):
        """
        Traverses that datastructure inside the MovieSystem

        :param func: is a function that needs to get executed on the objects
        preconditions: /
        postconditions: the input param func gets executed on the objects
        """
        self.datastruct.traverseTable(func)

    def retrieve(self, key):
        """
        Retrieves a key in the datastructure of Moviesystem

        :param key: is the searchkey
        preconditions: /
        postconditions: returns the objects or None and a bool (True if retrieve worked, else False)
        """
        return self.datastruct.tableRetrieve(key)

    def addMovie(self, title, rating, id=None):
        """
        Adds a movie to the MovieSystem.

        :optional param id: A unique number that corresponds to the Movie
        :param titel: The title of the movie
        :param rating: De score van een film volgens recensies.
        :return: True if succes, else False
        Pre-condition: /
        Post-condition: The movie with the given parameters gets saved to the system
        """
        if id is not None:
            self.count = max(self.count, id)
        id = self.count

        newMovie = Movie(id, title, rating)
        self.datastruct.tableInsert(newMovie.searchkey, newMovie)
        self.count += 1
        return True

    def removeAllMovies(self):
        """
        Removes all the Movies from the system

        Pre-condition: /
        Post-condition: All the movies got deleted from the system
        """
        self.count = 0
        self.datastruct = self.datastruct.__init__()

    def addIMBD(self):
        """
        Adds the top 250 movies from IMBD to the movieSytem

        preconditions: /
        postconditions: the top 250 movies from IMBD get loaded to the movieSytem
        """
        movies, ratings = getMovies()
        for title, rating in zip(movies, ratings):
            self.addMovie(title, rating)

    def query(self, searchkey, identifier):
        """
        Queries all the Movies corresponding to the searchkey and identifier

        possible identifiers:
            - "id"
            - "title"
            - "rating"

        :param searchkey: is the searchkey
        :param identifier: is the identified param you want to search on
        :return: returns a python list filled with items corresponding to the query
        """
        d = {
            "id": MaterializedIndex(self.datastruct, Movie.getId),
            "title": MaterializedIndex(self.datastruct, Movie.getTitle),
            "rating": MaterializedIndex(self.datastruct, Movie.getRating),
        }
        if identifier not in d:
            return None
        else:
            return d[identifier].query(searchkey)


# ADT for a Movie
class Movie:
    def __init__(self, id, title, rating):
        """
        Initializes a Movie object

        Pre-condition: /
        Post-condition: A Movie objects is created

        :param id: A unique number corresponding to the Movie object
        :param titel: The title of the Movie
        :param rating: A rating between 0 and 1, with a precision of 2 decimals
        """
        self.id = id
        self.title = title
        self.rating = rating

        from .Factories import SearchKeyFactory

        self.searchkey = SearchKeyFactory.getSearchkey("Movie")(self)

    def getId(self):
        """
        Getter for id

        preconditions: /
        postconditions: id gets returned

        :return: returns the id
        """
        return self.id

    def getTitle(self):
        """
        Getter for title

        preconditions: /
        postconditions: title gets returned

        :return: returns the title
        """
        return self.title

    def getRating(self):
        """
        Getter for rating

        preconditions: /
        postconditions: rating gets returned

        :return: returns the rating
        """
        return self.rating

    def getSearchkey(self):
        """
        Getter for searchKey

        preconditions: /
        postconditions: searchKey gets returned

        :return: returns the searchKey
        """
        return self.searchkey
