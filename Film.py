# Testen: Siebe
# Implementeren: Arne
class Film:
    id = 1
    def __init__(self, titel, rating):
        """
        Creëert een nieuwe film

        Preconditie: Rating moet tussen 0 en 10 zijn, moet een natuurlijk getal zijn en de titel een string

        Postconditie: Een nieuwe film is aangemaakt.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param titel: De titel van de film.
        :param rating: De score van een film volgens recensies.
        """
        self.id = Film.id  # Zet de id van de film gelijk aan de id
        Film.id += 1
        self.title = titel
        self.rating = rating

        print("added movie:", titel, sep=" ")

