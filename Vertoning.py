from Container import Container
# Testen: Cedric
# Implementeren: Sam
class Vertoningen(Container):
    def __init__(self, datastruct) -> None:
        super().__init__(datastruct)
    
    def addScreening(self, zaalnummer, slot, datum, filmid, vrijePlaatsen, id=None):
        """
        Voegt een vertoning toe aan het reservatiesysteem.
        Preconditie: De vertoning kan pas worden toegevoegd als er op hetzelfde slot
        en zaal nog geen andere vertoning is ingepland.
        Postconditie: De vertoning is toegevoegd aan het reservatiesysteem.
        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param zaalnummer: Het nummer van de zaal.
        :param slot: De tijd van de vertoning.
        :param datum: De datum van de vertoning.
        :param filmid: Dit is een uniek getal dat overeenkomt met de film.
        :param vrijePlaatsen: Het aantal vrije plaatsen.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        if id is None:
            id = self.count
        else:
            self.count = max(id, self.count)

        for i in range(0, self.count):
            temp = self.datastruct.tableRetrieve(i)[0]
            if temp is None:
                continue
            if temp.roomNumber == zaalnummer:
                if temp.date == datum:
                    if temp.slot == slot:
                        return False
        newScreening = Vertoning(id, zaalnummer, slot, datum, filmid, vrijePlaatsen)
        self.datastruct.tableInsert(self.datastruct.createItem(id, newScreening))
        self.count += 1

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
        self.reservedPlaces = 0
        self.seatedPlaces = 0

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

    def isReady(self):
        if self.reservedPlaces == self.seatedPlaces:
            return True
        return False