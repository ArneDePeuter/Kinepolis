from ADTfactory import ADTFactory
from Datastructuren.SAM.Datatypes import Hashmap

# Testen: Siebe
# Implementeren: Arne
class MovieSystem:
    def __init__(self) -> None:
        self.datastruct = ADTFactory.getADT("Movie")
        self.count = 0
        self.hashmap = Hashmap("sep",11)

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

        newMovie = Film(id, titel, rating)
        self.datastruct.tableInsert(newMovie.id, newMovie)
        self.count += 1

    def removeAllMovies(self):
        """
        Verwijderd alle films uit het reservatiesysteem.
        Preconditie: Er moet eerst een film bestaan voor er verwijderd kan worden
        Postconditie: Alle films zijn verwijderd uit het reservatiesysteem.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.count = 0
        self.datastruct = self.datastruct.__init__()

    def getSearchkey(self, Film):
        index = Film.Hashfunction()
        self.hashmap.insert(createTableItem(index,Film))
        hashmapIndex = index % self.hashmap.size
        LinkList = self.hashmap.map[hashmapIndex]
        secondIndex = 0
        while LinkList is not None:
            LinkList = LinkList.next
            secondIndex +=1
        return hashmapIndex,secondIndex



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

    def Hashfunction(self):
        index = 0
        for i in range(0, len(self.title)):
            index += ord(self.title)
        index = index % 11
        return index









"""
class Hashmovies:
    def __init__(self,key):
        self.hashmap = Hashmap("sep",11)
        self.hashkey = key

    def GetHashKey(self, Movie):
        if self.hashkey == "title":
            titel = Movie.title
            index = 0
            for i in range(0, len(titel)):
                index += ord(index[i])
            index1 = index%11
            index2 = 0
            iter = self.hashmap[index1]
            while iter is not None:
                iter = iter.next
                index2 +=1

"""



