from Datastructuren.ARNE.Wrappers.twoThreeTable import TwoThreeTreeTable as Table
# from ARNE.Wrappers.BSTTable import BSTTable as Table
from Datastructuren.ARNE.Wrappers.PrioQueue import PriorityQueue as Queue
from tijd import *

from Film import *
from Gebruiker import *
from Vertoning import *
from Zaal import *
from Reservatie import *

# Testen: Allemaal
# Implementeren: Allemaal
class Reservatiesysteem:
    def __init__(self):
        """
        Ceëert een reservatiesysteem.

        Preconditie: \
            
        Postconditie: Er is een reservatiesysteem aangemaakt.
        """
        self.users = Table()
        self.rooms = Table()
        self.movies = Table()
        self.screenings = Table()
        self.reservations = Queue()
        self.clock = Clock((0,0,0), (0,0,0))

        # Nummering for ID's
        self.userCount = 0
        self.movieCount = 0
        self.screeningCount = 0
        self.reservationCount = 0
        self.roomCount = 0

    def load(self):
        pass

    def save(self):
        pass

    def start(self):
        while not self.screenings.isEmpty():
            self.increaseTime(1)
            #handlereservations
            #handlescreenings
            #...
            pass

    def addUser(self, voornaam, achternaam, emailadres, id=None):
        """
        Voegt een gebruiker to aan het reservatiesysteem.

        Preconditie: De gebruiker mag nog niet bestaan in het systeem, based op dezelfde email

        Postconditie: Gebruiker is toegevoegd aan het reservatiesysteem.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param voornaam: De voornaam van de persoon.
        :param achternaam: De achternaam van de persoon.
        :param emailadres: Het e-mailadres van de persoon.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        if id is None:
            id = self.userCount+1
        else:
            self.userCount = id-1
        newUser = Gebruiker(id, voornaam, achternaam, emailadres)
        self.users.tableInsert(self.users.createItem(newUser.id, newUser))
        self.userCount += 1
        return True

    def removeAllUsers(self):
        """
        Verwijderd alle gebruikers uit het reservatiesysteem.

        Preconditie: Er moet eerst een gebruiker bestaan voor er verwijderd kan worden

        Postconditie: Alle gebruikers zijn verwijderd uit het reservatiesysteem.

        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.users = self.users.__init__()
        self.userCount = 0
    
    def addMovie(self, titel, rating, id=None):
        """
        Voegt een film toe aan het reservatiesysteem.

        Preconditie: De film moet nog niet bestaan in het systeem, based op dezelfde titel

        Postconditie: De film is toegevoegd aan het reservatiesysteem.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param titel: De titel van de film.
        :param rating: De score van een film volgens recensies.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        if id is None:
            id = self.movieCount+1
        else:
            self.movieCount = id-1
        newMovie = Film(id, titel, rating)
        self.movies.tableInsert(self.movies.createItem(newMovie.id, newMovie))
        self.movieCount += 1

    def removeAllMovies(self):
        """
        Verwijderd alle films uit het reservatiesysteem.

        Preconditie: Er moet eerst een film bestaan voor er verwijderd kan worden

        Postconditie: Alle films zijn verwijderd uit het reservatiesysteem.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.movieCount = 0
        self.movies = self.movies.__init__()

    def addRoom(self, zaalNummer, aantalPlaatsen):
        """
        Voegt een zaal toe aan het reservatiesysteem.

        Preconditie: \

        Postconditie: De zaal is toegevoegd aan het reservatiesysteem.
        Maar niet als er al een zaal bestaat met dezelfde nummer.

        :param room: De zaal die wordt toegevoegd.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        # TODO parameters juist zetten
        newRoom = Zaal(self.roomCount, aantalPlaatsen)
        self.roomCount += 1
        self.rooms.tableInsert(self.rooms.createItem(newRoom.id, newRoom))

    def addScreening(self, zaalnummer, slot, datum, filmid, vrijePlaatsen, id=None):
        """
        Voegt een vertoning toe aan het reservatiesysteem.

        Preconditie: De vertoning kan pas worden toegevoegd als er op hetzelfde slot
        en zaal nog geen andere vertoning is ingepland.

        Postconditie: De vertoning is toegevoegd aan het reservatiesysteem.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param zaalnummer: Het nummer van de zaal.
        :param slot: De tijd van de vertoning.
        :param datum: De datum van de vertoning.
        :param filmid: Dit is een uniek getal dat overeenkomt met de film.
        :param vrijePlaatsen: Het aantal vrije plaatsen.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        if id is None:
            id = self.screeningCount+1
        else:
            self.screeningCount = id-1
        for i in range(0, self.screeningCount):
            temp = self.screenings.tableRetrieve(i)
            if temp.roomNumber == zaalnummer:
                if temp.date == datum:
                    if temp.slot == slot:
                        return False
        newScreening = Vertoning(id, zaalnummer, slot, datum, filmid, vrijePlaatsen)
        self.screenings.tableInsert(self.screenings.createItem(newScreening.id, newScreening))
        self.screeningCount += 1

    def enqueueReservation(self, userid, timestamp, vertoningid, aantalPlaatsenGereserveerd):
        """
        Voegt een reservatie toe aan het reservatiesysteem.

        Preconditie: \

        Postconditie: De reservatie is toegevoegd aan het reservatiesysteem.

        :param reservering: De reservatie die wordt toegevoegd.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        # TODO parameters juist zetten
        newReservation = Reservatie(self.reservationCount, userid, timestamp, vertoningid, aantalPlaatsenGereserveerd)
        self.reservations.enqueue(self.reservations.createItem(newReservation.timestamp, newReservation))
        self.reservationCount += 1

    def dequeueReservation(self):
        """
        Geeft de eerst volgende reservatie.

        Preconditie: Er moet minstens één reservatie in het reservatiesysteem zitten.

        Postconditie: \

        :return: Tuple met True als de operatie is gelukt, False als het niet gelukt is en de eerstvolgend reservatie.
        """
        firstitem = self.reservations.dequeue()

    def removeAllReservations(self):
        """
        Verwijderd alle reservatie.

        Preconditie: \

        Postconditie: Alle reservaties zijn uit het reservatiesysteem verwijderd.

        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.reservations = self.reservations.__init__()
        self.reservationCount = 0

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

        :param n: Aantal seconden het syteem moet toenemen. Geen parameter doorgeven -> 1 seconden erbij
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.clock.tick(n) #tijd verhoogt met n seconden
