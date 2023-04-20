from .Factories import ADTFactory
from .MaterializedIndex import MaterializedIndex


# Testen: Siebe
# Implementeren: Arne
class RoomSystem:
    def __init__(self) -> None:
        """
        Initializes a RoomSystem

        Pre-condition : /
        Post-condition : A RoomSystem is created
        """
        self.datastruct = ADTFactory.getADT("Room")
        self.count = 0

    def traverse(self, func):
        """
         Traverses through the datastructure used in the RoomSystem

         :param func: function that gets executed on the objects
         precondition : RoomSystem is initialized
         postcondition : Input parameter function gets executed on objects
         """
        self.datastruct.traverseTable(func)

    def addRoom(self, numberPlaces, Roomnumber=None):
        """
        Add a room to the reservation system.

        Pre-condition:
        Post-condition: The room has been added to the reservation system.
        But not if a room with the same number already exists.
        :param Roomnumber: The room being added.
        :param numberPlaces: The number of seats that the room has.
        :return: True if the operation is successful, False if it fails.
        """
        if zaalNummer is not None:
            self.count = max(self.count, Roomnumber)

        newRoom = Room(self.count, numberPlaces)
        self.datastruct.tableInsert(newRoom.roomNumber, newRoom)
        self.count += 1

    def query(self, searchkey, identifier):
        """
        Queries all the Rooms corresponding to the searchkey and identifier

        possible identifiers:
            - "amountOfSeats"
            - "roomNumber"

        :param searchkey: is the searchkey
        :param identifier: is the identified param you want to search on
        :return: returns a python list filled with items corresponding to the query
        """
        d = {
            "roomNumber": MaterializedIndex(self.datastruct, Room.getRoomNumber),
            "amountOfSeats": MaterializedIndex(self.datastruct, Room.getAmountOfSeats),
        }
        if identifier not in d:
            return None
        else:
            return d[identifier].query(searchkey)


class Room:
    def __init__(self, roomNumber, numberPlaces):
        """
        Create a room.

        Pre-condition: The numberOfSeats and roomNumber are natural numbers.
        Post-condition: A room has been created.

        :param roomNumber: The number of the room.
        :param numberOfSeats: The number of seats in the room.
        """
        self.amountOfSeats = numberPlaces
        self.roomNumber = roomNumber

    def getAmountOfSeats(self):
        """
        Returns amount of seats

        Pre-condition: Room is initialized
        Post-condition: Amount of seats is returned
        """
        return self.amountOfSeats

    def getRoomNumber(self):
        """
        Returns roomnumber

        Pre-condition: Room is initialized
        Post-condition: Roomnumber is returned
        """
        return self.roomNumber
