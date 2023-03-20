from Container import Container
from ADTfactory import ADTFactory
from Datastructuren.ARNE.Wrappers.BSTTable import BSTTable as Table
# Testen: Sam
# Implementeren: Siebe
class UserSystem:
    def __init__(self) -> None:
        self.data = Table()

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
            id = self.count
        else:
            self.count = max(self.count,id)

        newUser = Gebruiker(id, voornaam, achternaam, emailadres)
        self.datastruct.tableInsert(self.datastruct.createItem(newUser.id, newUser))
        self.count += 1
        return True

    def removeAllUsers(self):
        """
        Verwijderd alle gebruikers uit het reservatiesysteem.
        Preconditie: Er moet eerst een gebruiker bestaan voor er verwijderd kan worden
        Postconditie: Alle gebruikers zijn verwijderd uit het reservatiesysteem.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.datastruct = self.datastruct.__init__()
        self.count = 0

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
        self.firstname = voornaam
        self.lastname = achternaam
        self.emailadres = emailadres
