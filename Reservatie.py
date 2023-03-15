#TODO: reservatie message specifieker
#TODO: reservatie mail specifieker

from Container import Container
from extra.mailsystem import MailSystem
# Testen: Arne
# Implementeren: Cedric
class ReservationSystem(Container):
    def __init__(self, screeningSystem, userSystem, datastruct=None) -> None:
        super().__init__(datastruct)
        self.screeningSystem = screeningSystem
        self.userSystem = userSystem
        self.mailsys = MailSystem()

    def reservate(self, userid, vertoningid, aantalPlaatsenGereserveerd):
        """
        Maakt een reservatie.
        Preconditie: \
        Postconditie: De reservatie is toegevoegd aan het reservatiesysteem.
        :param userid: id van de gebruiker die de reservatie maakt
        :param vertoningid: id van de vertoning
        :param aantalPlaatsenGereserveerd: het aantal plaatsen dat gereserveerd word door de reservering
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        # Zoeken op vertoningsID
        screening, succes = self.screeningSystem.datastruct.tableRetrieve(vertoningid)
        if not succes:
            print("Screening does not exist with this id")
            return False
        user, succes = self.userSystem.datastruct.tableRetrieve(userid)
        if not succes:
            print("User does not exist with this id")
            return False

        # if vertoning not full
        if screening.freePlaces >= aantalPlaatsenGereserveerd+screening.reservedPlaces:
            print(f"{aantalPlaatsenGereserveerd} places reservated for {vertoningid}")
            screening.reservedPlaces += aantalPlaatsenGereserveerd
            id = self.count
            # self.mailsys.sendMailTo("arne@depeuter.org", "The matrix", screening.slot, aantalPlaatsenGereserveerd, id)
            self.count += 1
            return True
        else:
            print("No free places")
            return False