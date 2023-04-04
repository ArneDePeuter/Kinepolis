from .Datastructuren.ARNE.Wrappers.BSTTable import BSTTable as Table


class User:
    def __init__(self, voornaam, achternaam, email) -> None:
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.email = email

    def __eq__(self, other) -> bool:
        return self is other

    def getVoornaam(self):
        return self.voornaam

    def getAchternaam(self):
        return self.achternaam

    def getEmail(self):
        return self.email

    def __str__(self) -> str:
        return f"{self.voornaam} : {self.achternaam} : {self.email}"


class MaterializedIndex:
    def __init__(self, table, identifier) -> None:
        self.dict = {}
        self.identifier = identifier
        table.traverseTable(self.setup)

    def setup(self, val):
        key = self.identifier(val)

        if key in self.dict:
            self.dict[key].append(val)
        else:
            self.dict[key] = [val]

    def query(self, searchKey):
        if searchKey in self.dict:
            return self.dict[searchKey]
        else:
            return []


if __name__ == "__main__":
    table = Table()

    u1 = User("Arne", "De Peuter", "arne@depeuter.org")
    u2 = User("Geert", "De Peuter", "geert@depeuter.org")
    u3 = User("Arne", "Hofkens", "arnehofkens@gmail.com")

    table.tableInsert(1, u1)
    table.tableInsert(2, u2)
    table.tableInsert(3, u3)

    achternaamIndex = MaterializedIndex(table, User.getAchternaam)
    voornaamIndex = MaterializedIndex(table, User.getVoornaam)
    depeuters = achternaamIndex.query("De Peuter")
    arnes = voornaamIndex.query("Arne")
    hofkens = achternaamIndex.query("Hofkens")

    print("De Peuters:")
    for depeuter in depeuters:
        print(str(depeuter))
    print()

    print("Hofkens:")
    for h in hofkens:
        print(str(h))
    print()

    print("Arne:")
    for arne in arnes:
        print(str(arne))
    print()

    print("Arne De Peuters: ")
    arneDePeuters = []
    for arne in arnes:
        if arne in depeuters:
            arneDePeuters.append(arne)
    for arneDp in arneDePeuters:
        print(str(arneDp))
