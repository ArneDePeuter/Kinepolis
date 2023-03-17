from Datastructuren.ARNE.Wrappers.twoThreeTable import TwoThreeTreeTable as Table

class ADTFactory: 
    def getADT(type):
        ADTDict = {
        "User" : Table,
        "Movie" : Table,
        "Screening": Table,
        "Room" : Table
        }
        return ADTDict[type]()