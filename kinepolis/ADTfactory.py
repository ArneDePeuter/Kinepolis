from .Datastructuren.ARNE.Wrappers.twoThreeTable import TwoThreeTreeTable as Table
from .Datastructuren.ARNE.Wrappers.PrioQueue import PriorityQueue as Queue
from .Datastructuren.SIEBE.Datatypes.MyLinkedChain import LinkedChain as LinkedList

class ADTFactory: 
    def getADT(type):
        ADTDict = {
        "User" : Table,
        "Movie" : Table,
        "Screening": Table,
        "Room" : Table,
        "Tickets" : Table, 
        "Events" : Queue,
        "Timestamps" : LinkedList
        }
        if type != "Events":
            return ADTDict[type]()
        else:
            return ADTDict[type](maxQueue=False)