from .ADTfactory import ADTFactory


# ADT that handles Events from Kinepolis class
class EventSystem:
    def __init__(self, system) -> bool:
        """
        Initializes the EventSystem

        param system: is the Kinepolis system the EventSystem depends on
        preconditions: Kinepolis is initalized
        postconditions: EventSystem is created
        """
        self.events = ADTFactory.getADT("Events")
        self.system = system
        self.reservationCount = 0

    def update(self):
        """
        Updates the event Queue

        preconditions: /
        postconditions: Top of the eventQueue gets executed when conditions are met
        """
        top, succes = self.events.dequeue()
        if not succes:
            return

        if top.timestamp <= self.system.clock:
            top.update(self)
            self.update()
        else:
            self.events.enqueue(top.timestamp, top)

    def addReservationEvent(self, userId, timestamp, screeningId, seats, id=None):
        foundUser = self.system.getUserSystem().retrieve(userId)[1]
        foundScreening = self.system.getScreeningSystem().retrieve(screeningId)[1]
        if not foundUser and not foundScreening:
            return False

        if id is not None:
            self.reservationCount = max(self.reservationCount, id)
        reservation = Reservation(
            timestamp, self.reservationCount, userId, screeningId, seats
        )
        self.events.enqueue(reservation.timestamp, reservation)
        self.reservationCount += 1
        return True

    def addLogEvent(self, timestamp, fileName):
        l = Log(timestamp, fileName)
        self.events.enqueue(l.timestamp, l)
        return True

    def addTicketEvent(self, timestamp, screeningId, seats):
        ticket = Ticket(screeningId, seats, timestamp)
        self.events.enqueue(ticket.timestamp, ticket)
        return True

    def addStartScreeningEvent(self, timestamp, screeningId):
        startScreening = StartScreening(timestamp, screeningId)
        self.events.enqueue(startScreening.timestamp, startScreening)
        return True

    def getEventList(self):
        items = []
        while not self.events.isEmpty():
            item, succes = self.events.dequeue()
            if succes:
                items.append(item)
        for item in items:
            self.events.enqueue(item.timestamp, item)
        return items


class Event:
    def __init__(self, timestamp, type, str) -> None:
        self.timestamp = timestamp
        self.object = object
        self.str = str
        self.type = type


class Ticket(Event):
    def __init__(self, screeningId, seats, timestamp) -> None:
        self.screeningId = screeningId
        self.seats = seats
        str = f"Seats: {seats} - ScreeningId: {screeningId}"
        super().__init__(timestamp, "Ticket", str)

    def update(self, eventSysem):
        eventSysem.system.getReservationSystem().useTicket(self.screeningId, self.seats)


class Log(Event):
    def __init__(self, timestamp, filename) -> None:
        self.filename = filename
        str = f"Filename: {filename}"
        super().__init__(timestamp, "Log", str)

    def update(self, eventSysem):
        eventSysem.system.save(self.filename)


class Reservation(Event):
    def __init__(self, timestamp, id, userId, screeningId, seats) -> None:
        self.id = id
        self.userId = userId
        self.timestamp = timestamp
        self.screeningId = screeningId
        self.seats = seats
        self.type = "Reservation"
        str = f"id:{id}, userId:{userId}, screeningId:{screeningId}, seats:{seats}"
        super().__init__(timestamp, "Reservation", str)

    def update(self, eventSysem):
        eventSysem.system.getReservationSystem().reservate(
            self.userId, self.screeningId, self.seats
        )
        eventSysem.reservationCount -= 1


class StartScreening(Event):
    def __init__(self, timestamp, screeningId) -> None:
        self.screeningID = screeningId
        str = f"ScreeningId:{screeningId}"
        super().__init__(timestamp, "Start Screening", str)

    def update(self, eventSystem):
        screening, succes = eventSystem.system.getScreeningSystem().retrieve(
            self.screeningID
        )
        if succes:
            screening.startScreening()
