class MaterializedIndex:
    def __init__(self, table, identifier) -> None:
        self.dict = {}
        self.identifier = identifier
        table.traverseTable(self.setup)

    def setup(self, val):
        if val is None:
            return
        
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