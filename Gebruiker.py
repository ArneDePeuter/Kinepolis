# Testen: Sam
# Implementeren: Siebe
class Gebruiker:
    id = 1
    def __init__(self, voornaam, achternaam, emailadres):
        """
        Ceëert een Gebruiker.

        Preconditie: voornaam is een string, achternaam is een string en emailadress is een string.

        Postconditie: Een nieuwe gebruiker is aangemaakt.

        :param id: Dit is een uniek getal dat overeenkomt met dit object.
        :param voornaam: De voornaam van de persoon.
        :param achternaam: De achternaam van de persoon.
        :param emailadres: Het e-mailadres van de persoon.
        """
        self.id = Gebruiker.id  # Zet de id van de film gelijk aan de id
        Gebruiker.id += 1
        self.firstname = voornaam
        self.lastname = achternaam
        self.emailadres = emailadres

        print("added user:", voornaam)
        pass

    def addReservation(self, reservatie):
        """
        Voegt de reservatie toe aan een gebruiker.

        Preconditie: \

        Postconditie: Gebruiker heeft een nieuwe reservatie.

        :param reservatie: De reservatie die toegevoegd wordt aan de gebruiker.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        pass

    def removeReservation(self, reservatie):
        """
        Verwijdert reservatie van een gebruiker.

        Preconditie: De gebruiker moet de reservatie hebben.

        Postconditie: De reservatie van de persoon is verwijderd.

        :param reservatie: De reservatie die wordt verwijderd van de gebruiker.
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        pass
