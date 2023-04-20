# Tests: All
# Implementation: All

from datetime import time as Time, datetime as Datetime, timedelta
from .Parser import Parser
from .Outputter import Outputter
from .Factories import ADTFactory

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
            
        Post-condition: A kinepolis reservation system is created.
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
        """
        Initializes timestamps into the Kinepolis system

        Pre-condition : Kinepolis is initialized
        Post-condition : Timestamps are imported into the kinepolis system
        """
        self.timestamps = ADTFactory.getADT("Timestamps")
        for i, time in enumerate(timestamps):
            self.timestamps.tableInsert(i, time)

    def save(self, filename):
        """
        Saves the whole system in a file with the given name.
        Pre-condition: Kinepolis is initialized
        Post-condition: Kinepolis system is exported into the given filename
        :param filename: name of the file where the system will be saved to.
        """
        self.outputter.generate(filename)

    def load(self, filename):
        """
        Loads data into the system.
        Pre-condition : System is initialized
        Post-condition : New data is loaded into the system
        :param filename: name of the file where the system will get the information from
        """
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
    
    def runSim(self):
        """
        Starts the kinepolis simulation and bursts trough all the events

        Pre-condition: /
        Post-condition: The eventqueue gets emptied inorder
        """
        while not self.eventSystem.isEmpty():
            self.eventSystem.update()
            self.skipToNextEvent()

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
        :param year: The year that the system should assume (optional parameter)
        :param month: The month that the system should assume (optional parameter)
        :param day: The day that the system should assume (optional parameter)
        :param hour: The hour that the system should assume (optional parameter)
        :param min: The minutes that the system should assume (optional parameter)
        :param sec: The seconds that the system should assume (optional parameter)
        :return: True if the operation succeeded, False if it did not succeed.
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
        Increases the time by n seconds.

        Pre-condition:
        Post-condition: The time of the system has been increased by n seconds.
        :param n: Number of seconds the system should increase. If no parameter is passed, increase by 1 second.
        :return: True if the operation succeeded, False if it did not succeed.
        """
        self.clock += timedelta(seconds=n)
        time.sleep(n)

    def getUserSystem(self):
        """
        Returns the UserSystem

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.userSystem

    def getMovieSystem(self):
        """
        Returns the MovieSystem

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.movieSystem

    def getRoomSystem(self):
        """
        Returns the RoomSystem

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.roomSystem

    def getScreeningSystem(self):
        """
        Returns the ScreeningSystem

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.screeningSystem

    def getReservationSystem(self):
        """
        Returns the ReservationSystem

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.reservationSystem

    def getEventSystem(self):
        """
        Returns the EventSystem

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.eventSystem

    def getTimeStamp(self, id):
        """
        Returns the TimeStamp

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.timestamps.tableRetrieve(id)
