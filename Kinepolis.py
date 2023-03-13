# Testen: Allemaal
# Implementeren: Allemaal

from Datastructuren.ARNE.Wrappers.twoThreeTable import TwoThreeTreeTable as Table
#from Datastructuren.ARNE.Wrappers.BSTTable import BSTTable as Table
from datetime import time as Time, datetime as DateTime
from Datastructuren.SIEBE.Datatypes.MyLinkedChain import LinkedChain as LinkedList
from Datastructuren.ARNE.Wrappers.PrioQueue import PriorityQueue as Queue
from Tests.Parser import Parser

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
        self.userSystem = UserSystem(Table())
        self.addUser = self.userSystem.addUser
        self.removeAllUsers = self.userSystem.removeAllUsers

        self.movieSystem = MovieSystem(Table())
        self.addMovie = self.movieSystem.addMovie
        self.removeAllMovies = self.movieSystem.removeAllMovies

        self.roomSystem = RoomSystem(Table())
        self.addRoom = self.roomSystem.addRoom

        self.screeningSystem = ScreeningSystem(Table())
        self.addScreening = self.screeningSystem.addScreening

        self.reservationSystem = ReservationSystem(Queue(), self.screeningSystem, self.userSystem)
        self.enqueueReservation = self.reservationSystem.enqueueReservation
        self.dequeueReservation = self.reservationSystem.dequeueReservation
        self.removeAllReservations = self.reservationSystem.removeAllReservations

        self.clock = DateTime(1,12,5)
        self.parser = Parser(self)

        #TIMESTAMPS
        self.timestamps = LinkedList()
        for i,time in enumerate([Time(14,30), Time(17), Time(20), Time(22,30), Time(00,30)]):
            self.timestamps.insert(i+1, time)

    def load(self, filename):
        self.parser.readFile(filename)

    def save(self, filename):
        self.parser.outputSystem(filename)

    def start(self):
        while not self.screenings.isEmpty():
            self.increaseTime(1)
            # handlereservations
            # handlescreenings
            # ...
            pass

    def setTime(self, time):
        """
        Zet de tijd van het reservatiesysteem.
        Preconditie: \
        Postconditie: De tijd van het reservatiesysteem is gelijk aan de gegeven tijd.
        :param time: De tijd die het systeem moet aannemen van het type Time.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.clock.setTime(time)

    def increaseTime(self, n=1):
        """
        Verhoogt de tijd n-seconden.
        Preconditie: \
        Postconditie: De tijd van het systeem is verhoogd met n-seconden.
        :param n: Aantal seconden het syteem moet toenemen. Geen parameter doorgeven → 1 seconden erbij
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.clock.tick(n)  # tijd verhoogt met n seconden

    def komBinnen(self, idvertoning, aantal):
        vertoning = self.screenings.tableRetrieve(idvertoning)[0]
        vertoning.seatedPlaces = vertoning.seatedPlaces + aantal
        if vertoning.isReady:
            vertoning.startScreening()
            return True
        else:
            return True