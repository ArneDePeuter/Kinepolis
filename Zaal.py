from Container import Container
# Testen: Siebe
# Implementeren: Arne
class Zalen(Container):
    def __init__(self, datastruct) -> None:
        super().__init__(datastruct)
    
    def addRoom(self, zaalNummer, aantalPlaatsen):
        """
        Voegt een zaal toe aan het reservatiesysteem.
        Preconditie: \
        Postconditie: De zaal is toegevoegd aan het reservatiesysteem.
        Maar niet als er al een zaal bestaat met dezelfde nummer.
        :param zaalNummer: De zaal die wordt toegevoegd.
        :param aantalPlaatsen: Het aantal plaatsen dat de zaal heeft.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        newRoom = Zaal(zaalNummer, aantalPlaatsen)
        self.datastruct.tableInsert(self.datastruct.createItem(newRoom.roomNumber, newRoom))

class Zaal:
    def __init__(self, zaalNummer, aantalPlaatsen):
        """
        Ceëert een zaal.

        Preconditie: Het aantalPlaatsen en zaalNummer zijn natuulrijke getallen.

        Postconditie: Een zaal is aangemaakt.

        :param zaalNummer: Het nummer van de zaal.
        :param aantalPlaatsen: Het aantal plaatsen in de zaal.
        """
        self.amountOfSeats = aantalPlaatsen
        self.roomNumber = zaalNummer

        print("created room:", zaalNummer)

    def enterRoom(self, reservation):
        """
        Voegt een het aantal personen van de reservering toe aan de zaal.

        Preconditie: Zaal mag niet vol zitten.

        Postconditie: Het aantal personen van de reservering is toegevoegd aan de zaal.

        :param reservation: De reservatie van de personen die in de zaal komen.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("Room has les free spaces.")
