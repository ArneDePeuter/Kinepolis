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
        from .Datastructuren.ARNE.Wrappers.PRIOQUEUE import PriorityQueue as PriorityQueueArne
        from .Datastructuren.ARNE.Wrappers.BSTTABLE import BSTTable as BSTtableArne
        from .Datastructuren.ARNE.Wrappers.TWOTHREETABLE import TwoThreeTreeTable as TTTtableArne
        from .Datastructuren.ARNE.Datatypes.LinkedList import LinkedList as LinkedListArne



        ADTDict = {
            "User": NonUniqueSearchkeyWrapper(BSTtableArne),
            "Movie": BSTtableArne(),
            "Screening": TTTtableArne(),
            "Room": BSTtableArne(),
            "Tickets": BSTtableArne(),
            "Events": PriorityQueueArne(),
            "Timestamps": TTTtableArne(),
            "NonUniqueList": LinkedListArne(),
        }
        return ADTDict[type]


class SearchKeyFactory:
    def getSearchkey(type):
        from .User import User
        from .Movie import Movie
        from .Screening import Screening
        """
        -> "User"
        -> "Movie"
        -> "Screening"
        """
        d = {"User": User.getFirstName, "Movie": Movie.getId, "Screening": Screening.getId}
        return d[type]
