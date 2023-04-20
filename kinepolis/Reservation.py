from .Extra.mailsystem import MailSystem

# Testen: Arne
# Implementeren: Cedric
class ReservationSystem:
    def __init__(self, system, sendMails) -> None:
        self.system = system
        self.mailsys = MailSystem()
        self.tickets = []
        self.reservationCount = 0
        self.sendMails = sendMails

    def reservate(self, userId, screeningId, seats):
        """
        Makes a reservation.
        Pre-condition: \
        Post-condition: The reservation is added to the system.
        :param userid: id of the user
        :param screeningId: id screening
        :param seats: amount of seats reserved
        :return: Returns if the operation was successful.
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
            if self.sendMails:
                movieName = self.system.getMovieSystem().retrieve(screening.filmsearchkey)[0].title
                self.mailsys.sendMailTo(user.emailadres, movieName, screening.timestamp, seats, screeningId)
            return True
        return False

    def useTicket(self, screeningId, seats):
        """
        Uses a ticket

        :param screeningId: id of the screening
        :param seats: the amount of seats
        Pre-conditions: /
        Post-conditions: Seats get taken in a screening
        :return: True if succes
        """
        if (screeningId, seats) not in self.tickets:
            return False
        vertoning, screeningExists = self.system.getScreeningSystem().retrieve(
            screeningId
        )
        if not screeningExists:
            return False
        vertoning.seatPlaces(seats, self.system.clock)
        if vertoning.status == "planned and ready":
            self.system.getEventSystem().addStartScreeningEvent(
                vertoning.timestamp, screeningId
            )
        return True
