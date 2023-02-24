# Testen: Arne
# Implementeren: Cedric

class Reservatie:
    def __init__(self, id, userid, timestamp, vertoningid, aantalPlaatsenGereserveerd):
        """
        Ceëert een reservatie.

        Preconditie: userid, vertoningid en aantalPlaatsenGereserveerd is een natuurlijk getal en de timestamp is geldig

        Postconditie: Een nieuwe reservatie is aangemaakt.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param userid: Het id van de gebruiker die de reservering maakt.
        :param timestamp: De tijd van de vertoning.
        :param vertoningid: Dit is een uniek getal dat overeenkomt met de vertonging van de reservering.
        :param aantalPlaatsenGereserveerd: Het aantal gereserveerde plaatsen.
        """
        self.id = id
        self.userid = userid
        self.timestamp = timestamp
        self.screeningid = vertoningid
        self.amountOfReservedSeats = aantalPlaatsenGereserveerd

    def __del__(self):
        pass
