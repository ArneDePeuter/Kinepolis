from Container import Container
# Testen: Arne
# Implementeren: Cedric
class ReservationSystem(Container):
    def __init__(self, datastruct, screeningSystem, userSystem) -> None:
        super().__init__(datastruct)
        self.screeningSystem = screeningSystem
        self.userSystem = userSystem
    
    def enqueueReservation(self, userid, timestamp, vertoningid, aantalPlaatsenGereserveerd):
        """
        Voegt een reservatie toe aan het reservatiesysteem.
        Preconditie: \
        Postconditie: De reservatie is toegevoegd aan het reservatiesysteem.
        :param userid: id van de gebruiker die de reservatie maakt
        :param timestamp: tijd wanneer de reservatie wordt gemaakt
        :param vertoningid: id van de vertoning
        :param aantalPlaatsenGereserveerd: het aantal plaatsen dat gereserveerd word door de reservering
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        # Zoeken op vertoningsID
        screening = self.screeningSystem.datastruct.tableRetrieve(vertoningid)[0]

        # if vertoning not full
        if screening.freePlaces >= aantalPlaatsenGereserveerd:
            newReservation = Reservatie(self.count, userid, timestamp, vertoningid,
                                        aantalPlaatsenGereserveerd)
            self.datastruct.enqueue(self.datastruct.createItem(newReservation.timestamp, newReservation))
            self.count += 1
            return True
        else:
            return False

    def dequeueReservation(self):
        """
        Geeft de eerst volgende reservatie.
        Preconditie: Er moet minstens één reservatie in het reservatiesysteem zitten.
        Postconditie: \
        :return: Tuple met True als de operatie is gelukt, False als het niet gelukt is en de eerstvolgend reservatie.
        """
        if self.datastruct == 0:
            return tuple((False, None))

        else:
            reservation = self.datastruct.dequeue()[1]
            screening = self.screeningSystem.datastruct.tableRetrieve(reservation.id)

            screening.freePlaces -= reservation.amountOfReservedSeats
            return tuple((True, reservation[1]))

    def removeAllReservations(self):
        """
        Verwijderd alle reservatie.
        Preconditie: \
        Postconditie: Alle reservaties zijn uit het reservatiesysteem verwijderd.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.datastruct = self.datastruct.__init__()
        self.count = 0

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
