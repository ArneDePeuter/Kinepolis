# Testen: Sam
# Implementeren: Siebe
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