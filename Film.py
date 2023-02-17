# Testen: Siebe
# Implementeren: Arne
class Film:
    def __init__(self, id, titel, rating):
        """
        Creëert een nieuwe film

        Preconditie: \

        Postconditie: Een nieuwe film is aangemaakt.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param titel: De titel van de film.
        :param rating: De score van een film volgens recensies.
        """
        self.id = id
        self.title = titel
        self.rating = rating

        print("added movie:", titel, sep=" ")

