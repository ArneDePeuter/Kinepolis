# Testen: Allemaal
# Implementeren: Allemaal

from datetime import time as Time, datetime as Datetime, timedelta
from .Parser import Parser
from .Outputter import Outputter
from .ADTfactory import ADTFactory

from .Film import MovieSystem
from .Gebruiker import UserSystem
from .Vertoning import ScreeningSystem
from .Zaal import RoomSystem
from .Reservatie import ReservationSystem
from .Event import EventSystem

import time

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
        self.screeningSystem = ScreeningSystem(self)

        self.reservationSystem = ReservationSystem(self)
        self.eventSystem = EventSystem(self)

        self.clock = Datetime(2023,3,31,10,59,40)
        self.parser = Parser(self)
        self.outputter = Outputter(self)

        self.initTimeStamps()

        self.running = False

    def initTimeStamps(self):
        self.timestamps = ADTFactory.getADT("Timestamps")
        for i,time in enumerate([Time(14,30), Time(17), Time(20), Time(22,30)]):
            self.timestamps.insert(i+1, time)

    def save(self, filename):
        """
        Slaagt het hele systeem op een een bestand met de gegeven bestandsnaam
        preconditie: /
        postconditie: /
        :param filename: naam van het bestand waar het systeem wordt opgeslagen
        """
        self.outputter.generate(filename)

    def load(self, filename):
        self.parser.readFile(filename)

    def start(self):
        """
        Start het systeem op
        preconditie: het systeem moet events bevatten
        postconditie: systeem is opgestart en de tijd van het systeem is verhoogd.
        """
        self.running = True
        while self.running:
            self.update()
    
    def update(self):
        if self.running:
            self.eventSystem.update()
            self.increaseTime()
    
    def skipToNextEvent(self):
        next, succes = self.eventSystem.events.dequeue()
        if not succes:
            return
        self.clock = next.timestamp
        self.eventSystem.events.enqueue(next.timestamp, next)

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
        time.sleep(n)

    def getUserSystem(self):
        return self.userSystem
    
    def getMovieSystem(self):
        return self.movieSystem
    
    def getRoomSystem(self):
        return self.roomSystem
    
    def getScreeningSystem(self):
        return self.screeningSystem
    
    def getReservationSystem(self):
        return self.reservationSystem
    
    def getEventSystem(self):
        return self.eventSystem
    
    def getTimeStamp(self, id):
        return self.timestamps.retrieve(int(id))