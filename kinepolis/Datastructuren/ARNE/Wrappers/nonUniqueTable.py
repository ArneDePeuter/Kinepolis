from ..Datatypes.struct_hashmap import Hashmap as Map
from ..Datatypes.struct_hashmap import createTableItem


class NonUniqueTable:
    def __init__(self) -> None:
        self.size = 997
        self.map = Map("sep", 997)

    def hashKey(self, key):
        total = 0
        for c in str(key):
            total += ord(c)
        return total % self.size

    def tableInsert(self, key, val):
        return self.map.tableInsert(createTableItem(self.hashKey(key), val))

    def tableRetrieve(self, key):
        return self.map.tableRetrieve(self.hashKey(key))
