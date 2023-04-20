class MaterializedIndex:
    def __init__(self, table, identifier) -> None:
        """
        Creates a Materializedindex Object
        :param table: is an ADT table
        :param identifier: is a getterFunction from the type inside the table
        Pre-conditions: /
        Post-conditions: MaterializedIndex object gets created
        """
        self.dict = {}
        self.identifier = identifier
        table.traverseTable(self.setup)

    def setup(self, val):
        """
        Sets up a value inside the object
        Pre-conditions: /
        Post-conditions: Sets up a value inside the object
        """
        if val is None:
            return
        
        key = self.identifier(val)

        if key in self.dict:
            self.dict[key].append(val)
        else:
            self.dict[key] = [val]

    def query(self, searchKey):
        """
        Queries the MaterializedIndex depending on the searchkey
        Pre-conditions: /
        Post-conditoins: /
        :return: Returns a list with all the objects corresponding to the searchKey 
        """
        if searchKey in self.dict:
            return self.dict[searchKey]
        else:
            return []