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