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

        Pre-condition: /
        Post-condition: returns the proper datastructure
        """
        #Wrapper for tables that expects non unique searchkeys
        from .NonUniqueWrap import NonUniqueWrap as NonUniqueSearchkeyWrapper

        #DataStructuren Arne
        from .Datastructuren.ARNE.Wrappers.PRIOQUEUE import PriorityQueue as PriorityQueue
        from .Datastructuren.ARNE.Wrappers.BSTTABLE import BSTTable as BSTtable
        from .Datastructuren.ARNE.Wrappers.TWOTHREETABLE import TwoThreeTreeTable as TTTtableArne
        from .Datastructuren.ARNE.Datatypes.LinkedList import LinkedList as LinkedListArne

        #DataStructuren Siebe
        #from .Datastructuren.SIEBE.Wrappers.BSTTable import BSTTable as BSTtable
        #from .Datastructuren.SIEBE.Wrappers.PrioQueue import PrioQueue as PriorityQueue


        ADTDict = {
            "User": BSTtable(),
            "Movie": BSTtable(),
            "Screening": TTTtableArne(),
            "Room": BSTtable(),
            "Tickets": BSTtable(),
            "Events": PriorityQueue(),
            "Timestamps": TTTtableArne(),
            "NonUniqueList": LinkedListArne(),
        }
        return ADTDict[type]


class SearchKeyFactory:
    def getSearchkey(type):
        """
        Returns the variable that's being used as the searchkey

        Pre-condition : Type is in dictionary
        Post-condition : Searchkey is returned

        """
        from .User import User
        from .Movie import Movie
        from .Screening import Screening
        """
        -> "User"
        -> "Movie"
        -> "Screening"
        """
        d = {"User": User.getId, "Movie": Movie.getId, "Screening": Screening.getId}
        return d[type]
