from DatatypesArne import TwoThreeTree as ttt

class FilmTable(ttt.TwoThreeTreeTable):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, obj):
        item = self.createTableItem(obj.id, obj)
        self.tableInsert(item)

class GebruikerTable(ttt.TwoThreeTreeTable):
    def __init__(self) -> None:
        super().__init__()
    
    def insert(self, obj):
        item = self.createTableItem(obj.id, obj)
        self.tableInsert(item)

class ReservatieTable(ttt.TwoThreeTreeTable):
    def __init__(self) -> None:
        super().__init__()
    
    def insert(self, obj):
        item = self.createTableItem(obj.id, obj)
        self.tableInsert(item)

class VertoningsTable(ttt.TwoThreeTreeTable):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, obj):
        item = self.createTableItem(obj.id, obj)
        self.tableInsert(item)

class ZaalTable(ttt.TwoThreeTreeTable):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, obj):
        item = self.createTableItem(obj.roomNumber, obj)
        self.tableInsert(item)