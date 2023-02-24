from DatatypesArne import struct_BST as BST
import univeralWrapper as wrapper

from Film import *
from Zaal import *

# Testen: Allemaal
# Implementeren: Allemaal
class Reservatiesysteem:
    def __init__(self):
        """
        Ceëert een reservatiesysteem.

        Preconditie: \
            
        Postconditie: Er is een reservatiesysteem aangemaakt.
        """
        self.users = wrapper.Wrapper(BST.BST(), wrapper.bst_dict)
        self.rooms = {}
        self.movies = {}
        self.screenings = {}
        self.reservations = {}
        self.time = 0

        self.userCount = 0
        self.movieCount = 0
        self.roomCount = 0
        self.screeningCount = 0
        self.reservationCount = 0

    def addUser(self, user):
        """
        Voegt een gebruiker to aan het reservatiesysteem.

        Preconditie: \

        Postconditie: Gebruiker is toegevoegd aan het reservatiesysteem.

        :param user: Gebruiker die wordt toegevoegd.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("Added user to database.")

        self.users.insert(BST.createTreeItem(user,user))

    def removeAllUsers(self):
        """
        Verwijderd alle gebruikers uit het reservatiesysteem.
        Preconditie: \

        Postconditie: Alle gebruikers zijn verwijderd uit het reservatiesysteem.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("All users removed.")

    def addMovie(self, titel, rating):
        """
        Voegt een film toe aan het reservatiesysteem.

        Preconditie: \

        Postconditie: De film is toegevoegd aan het reservatiesysteem.

        :param movie: De film die wordt toegevoegd.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """

        newMovie = Film(self.movieCount, titel, rating)
        self.movieCount += 1
        self.movies.insert(self.users.createTreeItem(newMovie, newMovie))
        print("Added movie to database.")
    
    def removeAllMovies(self):
        """
        Verwijderd alle films uit het reservatiesysteem.

        Preconditie: \

        Postconditie: Alle films zijn verwijderd uit het reservatiesysteem.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("All movies removed.")

    def addRoom(self, zaalNummer, aantalPlaatsen):
        """
        Voegt een zaal toe aan het reservatiesysteem.

        Preconditie: \

        Postconditie: De zaal is toegevoegd aan het reservatiesysteem.
        :param room: De zaal die wordt toegevoegd.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """

        newRoom = Zaal(self.roomCount, zaalNummer, aantalPlaatsen)
        self.roomCount += 1
        self.rooms.insert(self.rooms.createTreeItem(newRoom, newRoom))
        print("Room added to the database")

    def addScreening(self, screening):
        """
        Voegt een vertoning toe aan het reservatiesysteem.

        Preconditie: \

        Postconditie: De vertoning is toegevoegd aan het reservatiesysteem.

        :param screening: De vertoning die wordt toegevoegd.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("Added screening to database.")

    def addReservation(self, reservering):
        """
        Voegt een reservatie toe aan het reservatiesysteem.

        Preconditie: \

        Postconditie: De reservatie is toegevoegd aan het reservatiesysteem.

        :param reservering: De reservatie die wordt toegevoegd.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("Added reservation to database.")

    def queueReservation(self):
        """
        Geeft de eerst volgende reservatie.

        Preconditie: Er moet minstens één reservatie in het reservatiesysteem zitten.

        Postconditie: \

        :return: Tuple met True als de operatie is gelukt, False als het niet gelukt is en de eerstvolgend reservatie.
        """
        print("Leest de reservatie uit de queue.")

    def removeReservation(self, reservering):
        """
        Verwijderd de gegeven reservatie.

        Preconditie: De reservering moet in het reservatiesysteem zitten.

        Postconditie: De gegeven reservatie is verwijderd uit het reservatiesysteem.

        :param reservering: De reservering die moet worden verwijderd.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("Removed reservation to database.")

    def removeAllReservations(self):
        """
        Verwijderd alle reservatie.

        Preconditie: \

        Postconditie: Alle reservaties zijn uit het reservatiesysteem verwijderd.

        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("All reservations deleted.")

    def setTime(self, time):
        """
        Zet de tijd van het reservatiesysteem.

        Preconditie: \

        Postconditie: De tijd van het reservatiesysteem is gelijk aan de gegeven tijd.

        :param time: De tijd die het systeem moet aannemen.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("Time is set to", time)

    def increaseTime(self):
        """
        Verhoogt de tijd met een vaste waarde.

        Preconditie: \

        Postconditie: De tijd van het systeem is verhoogd met een vaste waarde.

        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        print("Time is increased.")