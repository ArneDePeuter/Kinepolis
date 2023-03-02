# Testen: Sam
# Implementeren: Siebe
from DatatypesSiebe.MyQueue import *
class Gebruiker:
    def __init__(self, id, voornaam, achternaam, emailadres):
        """
        Ceëert een Gebruiker.

        Preconditie: voornaam is een string, achternaam is een string en e-mailadres is een string.

        Postconditie: Een nieuwe gebruiker is aangemaakt.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param voornaam: De voornaam van de persoon.
        :param achternaam: De achternaam van de persoon.
        :param emailadres: Het e-mailadres van de persoon.
        """
        self.id = id
        self.id = Gebruiker.id  # Zet de id van de gebruiker gelijk aan de id
        Gebruiker.id += 1
        self.firstname = voornaam
        self.lastname = achternaam
        self.emailadres = emailadres
        self.reservaties = MyQueue(5)

    def addReservation(self, reservatie):
        """
        Voegt de reservatie toe aan een gebruiker.

        Preconditie: \

        Postconditie: Gebruiker heeft een nieuwe reservatie.

        :param reservatie: De reservatie die toegevoegd wordt aan de gebruiker.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.reservaties.enqueue(reservatie)

    def removeReservation(self):
        """
        Verwijdert de eerst volgende reservatie van een gebruiker.

        Preconditie: De gebruiker moet de reservatie hebben.

        Postconditie: De reservatie van de persoon is verwijderd.

        :param reservatie: De reservatie die wordt verwijderd van de gebruiker.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.reservaties.dequeue()
