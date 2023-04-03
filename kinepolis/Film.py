from .ADTfactory import ADTFactory
from .MaterializedIndex import MaterializedIndex
from .Datastructuren.SAM.Datatypes import Hashmap
from .Extra.movieWebScraper import getMovies

# Testen: Siebe
# Implementeren: Arne
class MovieSystem:
    def __init__(self) -> None:
        self.datastruct = ADTFactory.getADT("Movie")
        self.count = 0
        self.queries = {}

    def traverse(self, func):
        self.datastruct.traverseTable(func)
    
    def retrieve(self, key):
        return self.datastruct.tableRetrieve(key)

    def addMovie(self, titel, rating, id=None):
        """
        Voegt een film toe aan het reservatiesysteem.
        Preconditie: De film moet nog niet bestaan in het systeem, based op dezelfde titel
        Postconditie: De film is toegevoegd aan het reservatiesysteem.
        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param titel: De titel van de film.
        :param rating: De score van een film volgens recensies.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        if id is None:
            id = self.count
        else:
            self.count = max(self.count, id)
            id = self.count

        movies = self.query(titel, "title")
        if len(movies)!=0:
            return False
            
        newMovie = Film(id, titel, rating)
        self.datastruct.tableInsert(newMovie.id, newMovie)
        self.count += 1
        return True

    def removeAllMovies(self):
        """
        Verwijderd alle films uit het reservatiesysteem.
        Preconditie: Er moet eerst een film bestaan voor er verwijderd kan worden
        Postconditie: Alle films zijn verwijderd uit het reservatiesysteem.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.count = 0
        self.datastruct = self.datastruct.__init__()
    
    def addIMBD(self):
        movies, ratings = getMovies()
        for title, rating in zip(movies, ratings):
            self.addMovie(title, rating)
    
    def query(self, searchkey, identifier):
        d = {
            "id" : MaterializedIndex(self.datastruct, Film.getId),
            "title" : MaterializedIndex(self.datastruct, Film.getTitle),
            "rating" : MaterializedIndex(self.datastruct, Film.getRating),
        }
        if identifier not in d:
            return None
        else:
            return d[identifier].query(searchkey)

class Film:
    def __init__(self, id, titel, rating):
        """
        Creëert een nieuwe film

        Preconditie: Rating moet tussen 0 en 10 zijn, moet een natuurlijk getal zijn en de titel een string

        Postconditie: Een nieuwe film is aangemaakt.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param titel: De titel van de film.
        :param rating: De score van een film volgens recensies.
        """
        self.id = id
        self.title = titel
        self.rating = rating

    def __str__(self) -> str:
        return "titel: " + self.title + " rating: " + str(self.rating)
    
    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getRating(self):
        return self.rating


