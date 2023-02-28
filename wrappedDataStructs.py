from DatatypesArne import TwoThreeTree as ttt

USER_DATASTRUCT = ttt.TwoThreeTreeTable
ROOM_DATASTRUCT = ttt.TwoThreeTreeTable
MOVIE_DATASTRUCT = ttt.TwoThreeTreeTable
SCREENING_DATASTRUCT = ttt.TwoThreeTreeTable
RESERVATION_DATASTRUCT = ttt.TwoThreeTreeTable

def getWrapper(datastruct):
    class Wrapper(datastruct):
        def __init__(self) -> None:
            super().__init__()

        def insert(self, obj):
            item = self.createTableItem(obj.id, obj)
            self.tableInsert(item)

        def delete(self, searchkey):
            item = self.createTableItem(searchkey, "")
            self.tableDelete(item)
    
    return Wrapper()

users = getWrapper(USER_DATASTRUCT)
rooms = getWrapper(ROOM_DATASTRUCT)
movies = getWrapper(MOVIE_DATASTRUCT)
screenings = getWrapper(SCREENING_DATASTRUCT)
reservations = getWrapper(RESERVATION_DATASTRUCT)