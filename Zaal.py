# Testen: Siebe
# Implementeren: Arne
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
