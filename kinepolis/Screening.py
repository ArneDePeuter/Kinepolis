from .Factories import ADTFactory
from .MaterializedIndex import MaterializedIndex
from datetime import datetime, timedelta


# Testen: Cedric
# Implementeren: Sam
class ScreeningSystem:
    def __init__(self, system) -> None:
        """
        Initializes a ScreeningSystem

        precondition : /
        postcondition : a ScreeningSystem is created
        """
        self.datastruct = ADTFactory.getADT("Screening")
        self.system = system
        self.count = 0

    def traverse(self, func):
        """
        Traverses through the datastructure used in the ScreeningSystem

        :param func: function that gets executed on the objects
        precondition : ScreeningSystem is initialized
        postcondition : Input parameter function gets executed on objects
        """
        self.datastruct.traverseTable(func)

    def addScreening(self, RoomNumber, slot, Date, filmsearchkey, FreePlaces, id=None):
        """
        Adds a screening to the ScreeningSystem

        :param RoomNumber: The number of the room in which the screening is going to be played
        :param slot: The time slot of the screening
        :param Date: The date of the screening
        :param filmsearchkey: The searchkey of the movie
        :param FreePlaces: The amount of freeplaces in the room
        :param id: A unique number for that corresponds to the screening
        precondition : ScreeningSystem is initialized, the timestamp of the screening is in the future
        postcondition : A new screening is inserted into the ScreeningSystem
        """
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

        if timestamp < self.system.clock:
            return False

        newScreening = Screening(id, RoomNumber, timestamp, filmsearchkey, FreePlaces)
        self.datastruct.tableInsert(newScreening.searchkey, newScreening)
        self.count += 1
        return True

    def retrieve(self, searchkey):
        """
        Retrieves a searchkey from the datastructure from the ScreeningSystem

        :param searchkey: searchkey of a screening
        precondition : ScreeningSystem is initialized
        postcondition : returns object and true or none and false depending on whether the searchkey exists in the datastructure of the ScreeningSystem                         the searchkey exists inside of the datastructure
        """
        return self.datastruct.tableRetrieve(searchkey)

    def query(self, searchkey, identifier):
        """
        Queries all the Movies corresponding to the searchkey and identifier

        possible identifiers:
            - "id"

        :param searchkey: is the searchkey
        :param identifier: is the identified param you want to search on
        :return: returns a python list filled with items corresponding to the query
        """
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
        """
        Initializes a Screening object

        :param id: A unique number for that corresponds to the screening
        :param RoomNumber: The number of the room in which the screening is going to be played
        :param timestamp: Timestamp
        :param filmSearchkey: The searchkey of the movie
        :param FreePlaces: The amount of freeplaces in the room
        precondition: Correct types of inputs
        postcondition: Screening object was created
        """
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
        """
        Reserves places for the screening

        :param amount: Amount of places that are being reserved
        precondition: /
        postcondition: freePlaces is updated with the new correct number
        """
        if amount > self.freePlaces:
            return False
        self.freePlaces = self.freePlaces - amount
        return True

    def seatPlaces(self, amount, systemClock):
        """
        Seats people into their places

        :param amount: Amount of people that are being seated
        :param systemClock: Time of the system
        precondition: /
        postcondition: seatedPlaces is updated with the new correct number
        """
        self.seatedPlaces += amount
        self.updateStatus(systemClock)

    def startScreening(self):
        """
        Starts the screening

        precondition: /
        postcondition: Status of the screening is set to playing
        """
        self.status = "playing"

    def endScreening(self):
        """
        Ends the screening

        precondition: /
        postcondition: Status of the screening is set to ended
        """
        self.status = "ended"

    def updateStatus(self, systemClock):
        """
        Updates the status of the screening

        precondition : /
        postcondition: Status of the screening is updated
        """
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
        """
        Returns the status of a screening

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.status

    def getId(self):
        """
        Returns the id of a screening

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.id

    def getRoomNumber(self):
        """
        Returns the number of a room

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.roomNumber

    def getTimeStamp(self):
        """
        Returns the timestamp

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.timestamp

    def getFilmSearchkey(self):
        """
        Returns the filmsearchkey

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.filmsearchkey

    def getFreePlaces(self):
        """
        Returns the freeplaces

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.freePlaces

    def getReserverPlaces(self):
        """
        Returns the freeplaces

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.freePlaces

    def getReservedPlaces(self):
        """
        Returns the reservedplaces

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.reservedPlaces

    def getSeatedPlaces(self):
        """
        Returns the seatedplaces

        Precondition : The object exists
        Postcondition : Value of the attribute was returned
        """
        return self.seatedPlaces
