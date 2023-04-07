from .Factories import ADTFactory
from .MaterializedIndex import MaterializedIndex

# Testen: Sam
# Implementeren: Siebe
class UserSystem:
    def __init__(self) -> None:
        self.datastruct = ADTFactory.getADT("User")
        self.count = 0

    def retrieve(self, searchkey):
        return self.datastruct.tableRetrieve(searchkey)

    def traverse(self, func):
        self.datastruct.traverseTable(func)

    def addUser(self, voornaam, achternaam, emailadres, id=None):
        """
        Voegt een gebruiker to aan het reservatiesysteem.
        Pre-condition: De gebruiker mag nog niet bestaan in het systeem, based op dezelfde email
        Post-condition: User is toegevoegd aan het reservatiesysteem.
        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param voornaam: De voornaam van de persoon.
        :param achternaam: De achternaam van de persoon.
        :param emailadres: Het e-mailadres van de persoon.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        if id is None:
            id = self.count
        else:
            self.count = max(self.count, id)

        newUser = User(id, voornaam, achternaam, emailadres)
        self.datastruct.tableInsert(newUser.id, newUser)
        self.count += 1
        return True

    def removeAllUsers(self):
        """
        Verwijderd alle gebruikers uit het reservatiesysteem.
        Pre-condition: Er moet eerst een gebruiker bestaan voor er verwijderd kan worden
        Post-condition: Alle gebruikers zijn verwijderd uit het reservatiesysteem.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        self.datastruct = self.datastruct.__init__()
        self.count = 0

    def query(self, searchkey, identifier):
        d = {
            "id": MaterializedIndex(self.datastruct, User.getId),
            "firstname": MaterializedIndex(self.datastruct, User.getFirstName),
            "lastname": MaterializedIndex(self.datastruct, User.getLastName),
            "email": MaterializedIndex(self.datastruct, User.getEmail),
        }
        if identifier not in d:
            return None
        else:
            return d[identifier].query(searchkey)


class User:
    def __init__(self, id, voornaam, achternaam, emailadres):
        """
        Ceëert een User.

        Pre-condition: voornaam is een string, achternaam is een string en e-mailadres is een string.

        Post-condition: Een nieuwe gebruiker is aangemaakt.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param voornaam: De voornaam van de persoon.
        :param achternaam: De achternaam van de persoon.
        :param emailadres: Het e-mailadres van de persoon.
        """
        self.id = id
        self.firstname = voornaam
        self.lastname = achternaam
        self.emailadres = emailadres

        from .Factories import SearchKeyFactory
        self.searchkey = SearchKeyFactory.getSearchkey("User")(self)

    def getId(self):
        return self.id

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def getEmail(self):
        return self.emailadres
