from .Datastructuren.ARNE.Wrappers.twoThreeTable import TwoThreeTreeTable as Table
from .Datastructuren.ARNE.Wrappers.PrioQueue import PriorityQueue as Queue


# Factory class for ADT's
class ADTFactory:
    def getADT(type):
        """
        Returns the proper datastructure corresponding to the input parameter

        possible inputs:
            -"User"\n
            -"Movie" \n
            -"Room" \n
            -"Tickets" \n
            -"Events" \n
            -"Timestamps" \n

        precondition: /
        postcondition: returns the proper datastructure
        """
        ADTDict = {
            "User": Table,
            "Movie": Table,
            "Screening": Table,
            "Room": Table,
            "Tickets": Table,
            "Events": Queue,
            "Timestamps": Table,
        }
        if type != "Events":
            return ADTDict[type]()
        else:
            return ADTDict[type](maxQueue=False)
