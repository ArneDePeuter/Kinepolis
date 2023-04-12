from .Factories import ADTFactory
from .MaterializedIndex import MaterializedIndex
from datetime import datetime, timedelta


# Testen: Cedric
# Implementeren: Sam
class ScreeningSystem:
    def __init__(self, system) -> None:
        self.datastruct = ADTFactory.getADT("Screening")
        self.system = system
        self.count = 0

    def traverse(self, func):
        self.datastruct.traverseTable(func)

    def addScreening(self, RoomNumber, slot, Date, filmsearchkey, FreePlaces, id=None):
        if id is None:
            id = self.count
        else:
            self.count = max(id, self.count)

        timestamp, succes = self.system.getTimeStamp(slot)
        if not succes:
            return False

        timestamp = datetime(
            year=Date.year,
            month=Date.month,
            day=Date.day,
            hour=timestamp.hour,
            minute=timestamp.minute,
        )

        newScreening = Screening(id, RoomNumber, timestamp, filmsearchkey, FreePlaces)
        self.datastruct.tableInsert(newScreening.searchkey, newScreening)
        self.count += 1
        return True

    def retrieve(self, searchkey):
        return self.datastruct.tableRetrieve(searchkey)

    def query(self, searchkey, identifier):
        d = {
            "id": MaterializedIndex(self.datastruct, Screening.getId),
            "roomNumber": MaterializedIndex(self.datastruct, Screening.getRoomNumber),
            "slot": MaterializedIndex(self.datastruct, Screening.getSlot),
            "date": MaterializedIndex(self.datastruct, Screening.getDate),
            "filmsearchkey": MaterializedIndex(
                self.datastruct, Screening.getFilmSearchkey
            ),
            "freePlaces": MaterializedIndex(self.datastruct, Screening.getFreePlaces),
            "reservedPlaces": MaterializedIndex(
                self.datastruct, Screening.getReservedPlaces
            ),
            "seatedPlaces": MaterializedIndex(
                self.datastruct, Screening.getSeatedPlaces
            ),
            "status": MaterializedIndex(self.datastruct, Screening.getStatus),
        }
        if identifier not in d:
            return None
        else:
            return d[identifier].query(searchkey)


class Screening:
    def __init__(self, id, RoomNumber, timestamp, filmSearchkey, FreePlaces):
        self.id = id
        self.roomNumber = RoomNumber
        self.timestamp = timestamp
        self.filmsearchkey = filmSearchkey
        self.freePlaces = FreePlaces
        self.reservedPlaces = 0
        self.seatedPlaces = 0
        self.status = "planned"

        from .Factories import SearchKeyFactory

        self.searchkey = SearchKeyFactory.getSearchkey("Screening")(self)

    def reservePlaces(self, amount):
        if amount > self.freePlaces:
            return False
        self.freePlaces = self.freePlaces - amount
        return True

    def seatPlaces(self, amount, systemClock):
        self.seatedPlaces += amount
        self.updateStatus(systemClock)

    def startScreening(self):
        self.status = "playing"

    def endScreening(self):
        self.status = "ended"

    def updateStatus(self, systemClock):
        if self.timestamp > systemClock:
            if self.reservedPlaces == self.seatedPlaces:
                self.status = "planned and ready"
            else:
                self.status = "planned and waiting"
        else:
            if (
                self.reservedPlaces == self.seatedPlaces
                or self.status == "planned and ready"
            ):
                ScreeningTimePlusMovieTime = self.timestamp + timedelta(hours=2)
                if systemClock > ScreeningTimePlusMovieTime:
                    self.endScreening()
                else:
                    self.startScreening()
            else:
                self.status = "waiting"

    def getStatus(self):
        return self.status

    def getId(self):
        return self.id

    def getRoomNumber(self):
        return self.roomNumber

    def getTimeStamp(self):
        return self.timestamp

    def getFilmSearchkey(self):
        return self.filmsearchkey

    def getFreePlaces(self):
        return self.freePlaces

    def getReserverPlaces(self):
        return self.freePlaces

    def getReservedPlaces(self):
        return self.reservedPlaces

    def getSeatedPlaces(self):
        return self.seatedPlaces
