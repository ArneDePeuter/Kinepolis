# Testen: Allemaal
# Implementeren: Allemaal

from datetime import time as Time, datetime as Datetime, timedelta
from Datastructuren.SIEBE.Datatypes.MyLinkedChain import LinkedChain as LinkedList
from Datastructuren.ARNE.Wrappers.PrioQueue import PriorityQueue as Queue
from Parser import Parser

from Film import MovieSystem
from Gebruiker import UserSystem
from Vertoning import ScreeningSystem
from Zaal import RoomSystem
from Reservatie import ReservationSystem

class Kinepolis:
    def __init__(self):
        """
        Ceëert een reservatiesysteem.
        Preconditie: \
        Postconditie: Er is een reservatiesysteem aangemaakt.
        """
        self.userSystem = UserSystem()
        self.movieSystem = MovieSystem()
        self.roomSystem = RoomSystem()
        self.screeningSystem = ScreeningSystem()
        self.reservationSystem = ReservationSystem(self.screeningSystem, self.userSystem)

        self.clock = Datetime(2023,10,5,10,59,40)
        self.parser = Parser(self)

        #TIMESTAMPS
        self.timestamps = LinkedList()
        for i,time in enumerate([Time(14,30), Time(17), Time(20), Time(22,30)]):
            self.timestamps.insert(i+1, time)

        #SIM
        self.running = True
        self.events = Queue(maxQueue=False)

    def save(self, filename):
        """
        Slaagt het hele systeem op een een bestand met de gegeven bestandsnaam
        preconditie: /
        postconditie: /
        :param filename: naam van het bestand waar het systeem wordt opgeslagen
        """
        self.parser.outputSystem(filename, self.clock)

    def load(self, filename):
        self.parser.readFile(filename)
        if self.parser.events:
            self.start()

    def checkEvents(self):
        """
        # TODO wat doet deze functie?
        Preconditie:
        Postconditie:
        """
        while not self.events.isEmpty():
            event, succes = self.events.dequeue()
            if not succes: return

            if event.time <= self.clock:
                event.func()
            else:
                self.events.enqueue(event.time, event)
                return

    def start(self):
        """
        Start het systeem op
        preconditie: het systeem moet events bevatten
        postconditie: systeem is opgestart en de tijd van het systeem is verhoogd.
        """
        while self.running:
            self.checkEvents()
            self.increaseTime()

            if self.events.isEmpty():
                self.running = False

    def setTime(self, jaar = None, maand=None, dag=None, uur=None, min=None, sec=None):
        """
        Zet de tijd van het reservatiesysteem.
        Preconditie: \
        Postconditie: De tijd van het reservatiesysteem is gelijk aan de gegeven tijd.
        :param jaar: Het jaar dat het systeem moet aannemen (optioneele parameter)
        :param maand: Het maand dat het systeem moet aannemen (optioneele parameter)
        :param dag: De dag dat het systeem moet aannemen (optioneele parameter)
        :param uur: Het uur dat het systeem moet aannemen (optioneele parameter)
        :param min: De minuten dat het systeem moet aannemen (optioneele parameter)
        :param sec: De seconden dat het systeem moet aannemen (optioneele parameter)
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        jaar = jaar if jaar is not None else self.clock.year
        maand = maand if maand is not None else self.clock.month
        dag = dag if dag is not None else self.clock.day
        uur = uur if uur is not None else self.clock.hour
        min = min if min is not None else self.clock.minute
        sec = sec if sec is not None else self.clock.second
        self.clock = Datetime(jaar, maand, dag, uur, min, sec)
        return True

    def increaseTime(self, n=1):
        """
        Verhoogt de tijd n-seconden.
        Preconditie: \
        Postconditie: De tijd van het systeem is verhoogd met n-seconden.
        :param n: Aantal seconden het syteem moet toenemen. Geen parameter doorgeven → 1 seconden erbij
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.clock += timedelta(seconds=n)
        return True

    def komBinnen(self, idvertoning, aantal):
        """
        Verhoogt het aantal mensen die in een vertoning zitten met het gegeven aantal.
        preconditie: het aantal mag niet groter zijn dan het aantal vrije plaatsen voor de vertoning
        postconditie: het aantal vrije plaatsen van een vertoning is verminderd met het gegeven aantal
        """
        print(f"{aantal} people entered a room for {idvertoning}")
        vertoning = self.screeningSystem.datastruct.tableRetrieve(idvertoning)[0]
        vertoning.seatedPlaces = vertoning.seatedPlaces + aantal
        if vertoning.isReady():
            vertoning.startScreening()
            return True
        else:
            return True