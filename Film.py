# Testen: Siebe
# Implementeren: Arne
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

        print("created movie:", titel, sep=" ")
    
    def __str__(self) -> str:
        return "titel: " + self.title + " rating: " + str(self.rating)

