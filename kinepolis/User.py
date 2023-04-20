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
        Adds a user to the reservation system.
        Pre-condition: User must not yet exist in the system, based on the same email
        Post-condition: User is added to the booking system.
        :param id: This is a unique number corresponding to this object.
        :param voornaam: The first name of the person.
        :param achternaam: The surname of the person.
        :param emailadres: The person's email address.
        :return: True if the operation succeeded, False if it failed.
        """
        if id is None:
            id = self.count
        else:
            self.count = max(self.count, id)

        newUser = User(id, voornaam, achternaam, emailadres)
        self.datastruct.tableInsert(newUser.searchkey, newUser)
        self.count += 1
        return True

    def removeAllUsers(self):
        """
        Removes all users from the reservation system.
        Pre-condition: A user must exist before it can be deleted
        Post-condition: All users are removed from the reservation system.
        :return: True if the operation succeeded, False if it did not succeed.
        """
        self.datastruct = self.datastruct.__init__()
        self.count = 0

    def query(self, searchkey, identifier):
        """
        Returns all objects matching the search key and the identifier
        Pre-condition: /
        Post-condition: all objects matching the search key and the identifier gets returned
        :return: all objects matching the search key and the identifier
        """
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
        """
        Gets the id of the user

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.id

    def getFirstName(self):
        """
        Gets the firstname of the user

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.firstname

    def getLastName(self):
        """
        Gets the lastname of the user

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.lastname

    def getEmail(self):
        """
        Gets the e-mail of the user

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.emailadres
