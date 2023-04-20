from .Factories import ADTFactory


# ADT that handles Events from Kinepolis class
class EventSystem:
    def __init__(self, system) -> bool:
        """
        Initializes the EventSystem

        param system: is the Kinepolis system the EventSystem depends on
        Pre-conditions: Kinepolis is initialized
        Post-conditions: EventSystem is created
        """
        self.events = ADTFactory.getADT("Events")
        self.system = system
        self.reservationCount = 0
    
    def isEmpty(self):
        """
        Checks if there are events no left
        Pre-conditions: None
        Post-conditions: Returns True if there are no events left
        :return: True if Empty
        """
        return self.events.isEmpty()

    def update(self):
        """
        Updates the event Queue

        Pre-conditions: EventSystem is initialized
        Post-conditions: Top of the eventQueue gets executed when conditions are met
        """
        top, succes = self.events.dequeue()
        if not succes:
            return

        if top.timestamp <= self.system.clock:
            top.update(self)
            self.update()
        else:
            self.events.enqueue(top.timestamp, top)

    def addReservationEvent(self, userId, timestamp, screeningSearchkey, seats, id=None):
        """
        Adds a reservation event to the Queue

        :param userId: Id of the user that reserves tickets
        :param timestamp: Time when the user reserves the tickets
        :param screeningSearchkey: the searchkey of the screening
        :param seats: amount of seats that the person reserves
        :param id: unique number that corresponds to the reservation
        Pre-conditions: Eventsystem is initialized
        Post-conditions: Reservation is added to the event Queue
        :return: True if event added, False if not
        """
        foundUser = self.system.getUserSystem().retrieve(userId)[1]
        foundScreening = self.system.getScreeningSystem().retrieve(screeningSearchkey)[1]
        if not foundUser and not foundScreening:
            return False

        if id is not None:
            self.reservationCount = max(self.reservationCount, id)
        reservation = Reservation(
            timestamp, self.reservationCount, userId, screeningSearchkey, seats
        )
        self.events.enqueue(reservation.timestamp, reservation)
        self.reservationCount += 1
        return True

    def addLogEvent(self, timestamp, fileName):
        """
        Adds a log event to the EventSystem
        :param timestamp: is the timestamp on when the event takes place
        :param fileName: is the name of the log file
        Pre-conditions: Eventsystem is initialized
        Post-conditions: Log event is added to the EventSystem
        :return: True if event added
        """
        l = Log(timestamp, fileName)
        self.events.enqueue(l.timestamp, l)
        return True

    def addTicketEvent(self, timestamp, screeningId, seats):
        """
        Adds a ticket event to the EventSystem
        :param timestamp: is the timestamp on when the event takes place
        :param screeningId: is the id of the screening
        :param seats: is the amount of seats
        Pre-conditions: Eventsystem is initialized
        Post-conditions: Ticket event is added to the EventSystem
        :return: True if event added
        """
        ticket = Ticket(screeningId, seats, timestamp)
        self.events.enqueue(ticket.timestamp, ticket)
        return True

    def addStartScreeningEvent(self, timestamp, screeningId):
        """
        Adds a screening event to the EventSystem
        :param timestamp: is the timestamp on when the event takes place
        :param screeningId: is the id of the screening
        Pre-conditions: Eventsystem is initialized
        Post-conditions: Screening event is added to the EventSystem
        """
        startScreening = StartScreening(timestamp, screeningId)
        self.events.enqueue(startScreening.timestamp, startScreening)
        return True

    def getEventList(self):
        """
        Gets all the events in a list
        
        Pre-conditions: Eventsystem is initialized
        Post-conditions: Screening event is added to the EventSystem
        :return: a list with all the event items
        """
        items = []
        while not self.events.isEmpty():
            item, succes = self.events.dequeue()
            if succes:
                items.append(item)
        for item in items:
            self.events.enqueue(item.timestamp, item)
        return items

#ADT for an Event
class Event:
    def __init__(self, timestamp, type, str) -> None:
        """
        Creates an Event object
        :param timestamp: the time the event takes place
        :param type: is the type of the event
        :param str: is the string repr of the event
        Pre-conditions: /
        Post-conditions: Event object gets created
        """
        self.timestamp = timestamp
        self.object = object
        self.str = str
        self.type = type


class Ticket(Event):
    def __init__(self, screeningId, seats, timestamp) -> None:
        """
        Creates a Ticket Event object
        :param screeningId: the id of the screening
        :param seats: the amount of seats
        :param timestamp: the time the event takes place
        Pre-conditions: /
        Post-conditions: TicketEvent object gets created
        """
        self.screeningId = screeningId
        self.seats = seats
        string = f"Seats: {seats} - ScreeningId: {screeningId}"
        super().__init__(timestamp, "Ticket", string)

    def update(self, eventSysem):
        """
        Updates the event
        Pre-conditions: /
        Post-conditions: Event gets updated
        """ 
        eventSysem.system.getReservationSystem().useTicket(self.screeningId, self.seats)


class Log(Event):
    def __init__(self, timestamp, filename) -> None:
        """
        Creates a Ticket Event object
        :param screeningId: the id of the screening
        :param seats: the amount of seats
        :param timestamp: the time the event takes place
        Pre-conditions: /
        Post-conditions: TicketEvent object gets created
        """
        self.filename = filename
        string = f"Filename: {filename}"
        super().__init__(timestamp, "Log", string)

    def update(self, eventSysem):
        """
        Updates the event
        Pre-conditions: /
        Post-conditions: Event gets updated
        """ 
        eventSysem.system.save(self.filename)


class Reservation(Event):
    def __init__(self, timestamp, id, userId, screeningId, seats) -> None:
        """
        Creates a Reservation Event object
        :param id: the id of the reservation
        :param userId: the id of the user
        :param seats: the amount of seats
        :param screeningId: the id of the screening
        :param timestamp: the time the event takes place
        Pre-conditions: /
        Post-conditions: ReservationEvent object gets created
        """
        self.id = id
        self.userId = userId
        self.timestamp = timestamp
        self.screeningId = screeningId
        self.seats = seats
        self.type = "Reservation"
        string = f"id:{id}, userId:{userId}, screeningId:{screeningId}, seats:{seats}"
        super().__init__(timestamp, "Reservation", string)

    def update(self, eventSysem):
        """ 
        Updates the event
        Pre-conditions: /
        Post-conditions: Event gets updated
        """ 
        eventSysem.system.getReservationSystem().reservate(
            self.userId, self.screeningId, self.seats
        )
        eventSysem.reservationCount -= 1


class StartScreening(Event):
    def __init__(self, timestamp, screeningId) -> None:
        """
        Creates a Reservation Event object
        :param screeningId: the id of the screening
        :param timestamp: the time the event takes place
        Pre-conditions: /
        Post-conditions: ReservationEvent object gets created
        """
        self.screeningID = screeningId
        string = f"ScreeningId:{screeningId}"
        super().__init__(timestamp, "Start Screening", string)

    def update(self, eventSystem):
        """
        Updates the event
        Pre-conditions: /
        Post-conditions: Event gets updated
        """ 
        screening, succes = eventSystem.system.getScreeningSystem().retrieve(
            self.screeningID
        )
        if succes:
            screening.startScreening()
