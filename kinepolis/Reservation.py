# TODO: reservatie message specifieker
# TODO: reservatie mail specifieker

from .Extra.mailsystem import MailSystem


# Testen: Arne
# Implementeren: Cedric
class ReservationSystem:
    def __init__(self, system) -> None:
        self.system = system
        self.mailsys = MailSystem()
        self.tickets = []
        self.reservationCount = 0

    def reservate(self, userId, screeningId, seats):
        """
        Maakt een reservatie.
        Pre-condition: \
        Post-condition: De reservatie is toegevoegd aan het reservatiesysteem.
        :param userid: id van de gebruiker die de reservatie maakt
        :param vertoningid: id van de vertoning
        :param seats: het aantal plaatsen dat gereserveerd word door de reservering
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """

        # Zoeken op vertoningsID
        screening, succes = self.system.getScreeningSystem().retrieve(screeningId)
        if not succes:
            return False
        user, succes = self.system.getUserSystem().retrieve(userId)
        if not succes:
            return False

        # if vertoning not full
        if screening.freePlaces >= seats + screening.reservedPlaces:
            screening.reservedPlaces += seats
            self.tickets.append((screeningId, seats))
            movieName = self.system.getMovieSystem().retrieve(screening.filmsearchkey)
            self.mailsys.sendMailTo("arne@depeuter.org", movieName, screening.slot, seats, screeningId)
            return True
        else:
            return False

    def useTicket(self, idvertoning, aantal):
        if (idvertoning, aantal) not in self.tickets:
            return False
        vertoning, screeningExists = self.system.getScreeningSystem().retrieve(
            idvertoning
        )
        if not screeningExists:
            return False
        vertoning.seatPlaces(aantal, self.system.clock)
        if vertoning.status == "planned and ready":
            self.system.getEventSystem().addStartScreeningEvent(
                vertoning.timestamp, idvertoning
            )
        return True
