# Tests: All
# Implementation: All

from datetime import time as Time, datetime as Datetime, timedelta
from .Parser import Parser
from .Outputter import Outputter
from .ADTfactory import ADTFactory

from .Movie import MovieSystem
from .User import UserSystem
from .Screening import ScreeningSystem
from .Room import RoomSystem
from .Reservation import ReservationSystem
from .Event import EventSystem

import time


class Kinepolis:
    def __init__(self):
        """
        Creates a reservation system.
        Pre-condition: \
            
        Post-condition: A reservation system is created.
        """
        self.userSystem = UserSystem()
        self.movieSystem = MovieSystem()
        self.roomSystem = RoomSystem()
        self.screeningSystem = ScreeningSystem(self)

        self.reservationSystem = ReservationSystem(self)
        self.eventSystem = EventSystem(self)

        now = Datetime.now()
        current_time = Datetime(now.year, now.month, now.day, now.hour, now.minute)
        self.clock = current_time

        self.parser = Parser(self)
        self.outputter = Outputter(self)

        self.timestamps = None
        self.initTimeStamps([Time(14, 30), Time(17), Time(20), Time(22, 30)])

        self.running = False

    def initTimeStamps(self, timestamps):
        self.timestamps = ADTFactory.getADT("Timestamps")
        for i, time in enumerate(timestamps):
            self.timestamps.tableInsert(i, time)

    def save(self, filename):
        """
        Saves the whole system in a file with the given name.
        Pre-condition: /
        Post-condition: /
        :param filename: name of the file where the system will be saved to.
        """
        self.outputter.generate(filename)

    def load(self, filename):
        self.parser.readFile(filename)

    def start(self):
        """
        Starts the system
        Pre-condition: The system has to have events.
        Post-condition: System has started and will keep updating until it is shut down.
        """
        self.running = True
        while self.running:
            self.update()

    def update(self):
        """
        Updates the system
        Pre-condition: system.running is set to true
        Post-condition: system events are updated and the time of the system is increased.
        """
        if self.running:
            self.eventSystem.update()
            self.increaseTime()

    def skipToNextEvent(self):
        """
        Skips system to conditions of for the next system event.
        Pre-condition: System has to have events.
        Post-condition: System conditions are set to the conditions for the next event.
        """
        next, succes = self.eventSystem.events.dequeue()
        if not succes:
            return
        self.clock = next.timestamp
        self.eventSystem.events.enqueue(next.timestamp, next)

    def setTime(self, year=None, month=None, day=None, hour=None, min=None, sec=None):
        """
        Sets the time and date of the system.
        Pre-condition: \
        Post-condition: The time of the system is equal to the given time and date
        :param year: Het jaar dat het systeem moet aannemen (optionele parameter)
        :param month: Het maand dat het systeem moet aannemen (optionele parameter)
        :param day: De dag dat het systeem moet aannemen (optionele parameter)
        :param hour: Het uur dat het systeem moet aannemen (optionele parameter)
        :param min: De minuten dat het systeem moet aannemen (optionele parameter)
        :param sec: De seconden dat het systeem moet aannemen (optionele parameter)
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        year = year if year is not None else self.clock.year
        month = month if month is not None else self.clock.month
        day = day if day is not None else self.clock.day
        hour = hour if hour is not None else self.clock.hour
        min = min if min is not None else self.clock.minute
        sec = sec if sec is not None else self.clock.second
        self.clock = Datetime(year, month, day, hour, min, sec)
        return True

    def increaseTime(self, n=1):
        """
        Verhoogt de tijd n-seconden.
        Pre-condition: \
        Post-condition: De tijd van het systeem is verhoogd met n-seconden.
        :param n: Aantal seconden het systeem moet toenemen. Geen parameter doorgeven → 1 seconden erbij
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
        return self.timestamps.tableRetrieve(id)
