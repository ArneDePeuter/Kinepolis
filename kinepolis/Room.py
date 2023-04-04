from .ADTfactory import ADTFactory
from .MaterializedIndex import MaterializedIndex


# Testen: Siebe
# Implementeren: Arne
class RoomSystem:
    def __init__(self) -> None:
        self.datastruct = ADTFactory.getADT("Room")
        self.count = 0

    def traverse(self, func):
        self.datastruct.traverseTable(func)

    def addRoom(self, aantalPlaatsen, zaalNummer=None):
        """
        Voegt een zaal toe aan het reservatiesysteem.
        Pre-condition: \
        Post-condition: De zaal is toegevoegd aan het reservatiesysteem.
        Maar niet als er al een zaal bestaat met dezelfde nummer.
        :param zaalNummer: De zaal die wordt toegevoegd.
        :param aantalPlaatsen: Het aantal plaatsen dat de zaal heeft.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        if zaalNummer is not None:
            self.count = max(self.count, zaalNummer)

        newRoom = Room(self.count, aantalPlaatsen)
        self.datastruct.tableInsert(newRoom.roomNumber, newRoom)
        self.count += 1

    def query(self, searchkey, identifier):
        d = {
            "roomNumber": MaterializedIndex(self.datastruct, Room.getRoomNumber),
            "amountOfSeats": MaterializedIndex(self.datastruct, Room.getAmountOfSeats),
        }
        if identifier not in d:
            return None
        else:
            return d[identifier].query(searchkey)


class Room:
    def __init__(self, zaalNummer, aantalPlaatsen):
        """
        Ceëert een zaal.

        Pre-condition: Het aantalPlaatsen en zaalNummer zijn natuulrijke getallen.

        Post-condition: Een zaal is aangemaakt.

        :param zaalNummer: Het nummer van de zaal.
        :param aantalPlaatsen: Het aantal plaatsen in de zaal.
        """
        self.amountOfSeats = aantalPlaatsen
        self.roomNumber = zaalNummer

    def getAmountOfSeats(self):
        return self.amountOfSeats

    def getRoomNumber(self):
        return self.roomNumber
