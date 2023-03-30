from .ADTfactory import ADTFactory
from .MaterializedIndex import MaterializedIndex
from datetime import datetime

# Testen: Cedric
# Implementeren: Sam
class ScreeningSystem:
    def __init__(self, system) -> None:
        self.datastruct=ADTFactory.getADT("Screening")
        self.system = system
        self.count = 0
    
    def traverse(self, func):
        self.datastruct.traverseTable(func)

    def addScreening(self, zaalnummer, slot, datum, filmid, vrijePlaatsen, id=None):
        if id is None:
            id = self.count
        else:
            self.count = max(id, self.count)

        timestamp, succes = self.system.getTimeStamp(slot)
        if not succes:
            return False
        
        timestamp = datetime(year=datum.year, month=datum.month, day=datum.day, hour=timestamp.hour, minute=timestamp.minute)

        newScreening = Vertoning(id, zaalnummer, timestamp, filmid, vrijePlaatsen)
        self.datastruct.tableInsert(id, newScreening)
        self.count += 1
        return True
    
    def retrieve(self, searchkey):
        return self.datastruct.tableRetrieve(searchkey)
    
    def query(self, searchkey, identifier):
        d = {
            "id" : MaterializedIndex(self.datastruct, Vertoning.getId),
            "roomNumber" : MaterializedIndex(self.datastruct, Vertoning.getRoomNumber),
            "slot" : MaterializedIndex(self.datastruct, Vertoning.getSlot),
            "date" : MaterializedIndex(self.datastruct, Vertoning.getDate),
            "filmid" : MaterializedIndex(self.datastruct, Vertoning.getFilmId),
            "freePlaces" : MaterializedIndex(self.datastruct, Vertoning.getFreePlaces),
            "reservedPlaces" : MaterializedIndex(self.datastruct, Vertoning.getReservedPlaces),
            "seatedPlaces" : MaterializedIndex(self.datastruct, Vertoning.getSeatedPlaces),
            "status" : MaterializedIndex(self.datastruct, Vertoning.getStatus)
        }
        if identifier not in d:
            return None
        else:
            return d[identifier].query(searchkey)
        
class Vertoning:
    def __init__(self, id, zaalnummer, timestamp, filmid, vrijePlaatsen):
        self.id = id
        self.roomNumber = zaalnummer
        self.timestamp = timestamp
        self.filmid = filmid
        self.freePlaces = vrijePlaatsen
        self.reservedPlaces = 0
        self.seatedPlaces = 0
        self.status = "planned"

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
        if self.timestamp>systemClock:
            if self.reservedPlaces == self.seatedPlaces:
                self.status = "planned and ready"
        else:
            if self.reservedPlaces == self.seatedPlaces or self.status=="planned and ready" :
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
    
    def getFilmId(self):
        return self.filmid
    
    def getFreePlaces(self):
        return self.freePlaces
    
    def getReserverPlaces(self):
        return self.freePlaces
    
    def getReservedPlaces(self):
        return self.reservedPlaces
    
    def getSeatedPlaces(self):
        return self.seatedPlaces