from Container import Container
from ADTfactory import ADTFactory

# Testen: Siebe
# Implementeren: Arne
class MovieSystem(Container):
    def __init__(self) -> None:
        super().__init__(datastruct=ADTFactory.getADT("Movie"))

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
        self.datastruct.tableInsert(self.datastruct.createItem(newMovie.id, newMovie))
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
