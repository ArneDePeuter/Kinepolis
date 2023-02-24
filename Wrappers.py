from DatatypesArne import struct_23Tree as tree

class FilmTable(tree.TwoThreeTreeTable):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, obj):
        item = self.createTableItem(obj.id, obj)
        self.tableInsert(item)

class GebruikerTable(tree.TwoThreeTreeTable):
    def __init__(self) -> None:
        super().__init__()
    
    def insert(self, obj):
        item = self.createTableItem(obj.id, obj)
        self.tableInsert(item)

class ReservatieTable(tree.TwoThreeTreeTable):
    def __init__(self) -> None:
        super().__init__()
    
    def insert(self, obj):
        item = self.createTableItem(obj.id, obj)
        self.tableInsert(item)

class VertoningsTable(tree.TwoThreeTreeTable):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, obj):
        item = self.createTableItem(obj.id, obj)
        self.tableInsert(item)

class ZaalTable(tree.TwoThreeTreeTable):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, obj):
        item = self.createTableItem(obj.roomNumber, obj)
        self.tableInsert(item)