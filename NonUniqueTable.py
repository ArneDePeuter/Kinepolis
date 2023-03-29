from Datastructuren.ARNE.Wrappers.BSTTable import BSTTable as Table

class User:
    def __init__(self, voornaam, achternaam, id) -> None:
        self.id = id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.uniqueSearchkey = self.id
    
    def __str__(self):
        return f"id = {self.id} : voornaam = {self.voornaam} : achternaam = {self.achternaam}"

class NonUniqueTable:
    def __init__(self, tableType) -> None:
        self.tableType = tableType
        self.map = {}

    def tableInsert(self, key, val):
        if key in self.map:
            self.map[key].tableInsert(val.uniqueSearchkey, val)
        else:
            self.map[key] = self.tableType()
            self.map[key].tableInsert(val.uniqueSearchkey, val)
    
    def tableRetrieve(self, key):
        if key in self.map:
            l = []
            self.map[key].traverseTable(l.append)
            if len(l)>0:
                return l[0], True
        return None, False

if __name__ == "__main__":
    voornaamTable = NonUniqueTable(Table)

    u1 = User("Arne", "De Peuter", 0)
    u2 = User("Arne", "Hofkens", 1)

    voornaamTable.tableInsert(u1.voornaam, u1)
    voornaamTable.tableInsert(u2.voornaam, u2)

    print(voornaamTable.tableRetrieve("Arne")[0])

    achterNaamTable = NonUniqueTable(Table)

    achterNaamTable.tableInsert(u1.achternaam, u1)
    achterNaamTable.tableInsert(u2.achternaam, u2)

    print(achterNaamTable.tableRetrieve("Hofkens")[0])