# Testen: Cedric
# Implementeren: Sam
class Vertoning:
    def __init__(self, id, zaalnummer, slot, datum, filmid, vrijePlaatsen):
        """
        Ceëert een vertoning.

        Preconditie: De zaalummer, filmid, vrijePlaatsen zijn een naturlijke getallen en het slot en de datum zijn geldig

        Postconditie: Een vertoning is aangemaakt.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param zaalnummer: Het nummer van de zaal.
        :param slot: De tijd van de vertoning.
        :param datum: De datum van de vertoning.
        :param filmid: Dit is een uniek getal dat overeenkomt met de film.
        :param vrijePlaatsen: Het aantal vrije plaatsen.
        """
        self.id = id
        self.roomNumber = zaalnummer
        self.slot = slot
        self.date = datum
        self.filmid = filmid
        self.freePlaces = vrijePlaatsen

        print("created screening at", slot, "in room", zaalnummer, sep=" ")

    def startScreening(self):
        """
        Start de vertoning.

        Preconditie: Alle mensen met een reservering moeten in de zaal zitten.

        Postconditie: De vertoning start.

        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("Movie is started.")

    def reservePlaces(self, amount):
        """
        implementatie van sam... arne heeft dit nodig
        """
        if amount > self.freePlaces:
            return False
        self.freePlaces = self.freePlaces - amount
        return True

    def endScreening(self):
        """
        Stop de vertoning.

        Preconditie: Vertoning moet gestart zijn.

        Postconditie: De vertoning stopt, alle gebruikers worden uit de zaal gezet.

        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("Movie ended, room is cleared.")
