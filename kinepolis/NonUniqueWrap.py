from .Factories import ADTFactory


# ADT that makes it possible to use nonunique searchkeys
class NonUniqueWrap:
    def __init__(self, table) -> None:
        """
        Initializes the wrapper

        preconditions: /
        postconditions: a table gets created that can handle nonUnique searchKeys
        :param table: is the table that needs to get modified
        """
        self.table = table()

    def tableInsert(self, key, val):
        """
        Inserts a value accordingly to the key

        preconditions: NonUniqueWrap is initialized
        postconditions: If worked, the value is added and True is returned. Else returns False.
        :param key: is the searchkey
        :param val: is the value that needs to get inserted
        :return: True if insertion worked, else False
        """
        if self.table.tableIsEmpty():
            newList = ADTFactory.getADT("NonUniqueList")
            newList.insert(newList.size + 1, val)
            return self.table.tableInsert(key, newList)

        item, succes = self.table.tableRetrieve(key)
        if succes:
            return item.insert(item.size + 1, val)
        else:
            newList = ADTFactory.getADT("NonUniqueList")
            newList.insert(newList.size + 1, val)
            return self.table.tableInsert(key, newList)

    def traverseTable(self, func):
        """
        Traverses the table inorder and the func gets applied to every item

        preconditions: NonUniqueWrap is initialized
        postconditions: func gets applied to every item inorder
        """
        l = []
        self.table.traverseTable(l.append)
        items = []
        for LLitem in l:
            items.extend(list(LLitem.save()))
        for item in items:
            func(item)

    def tableRetrieve(self, key):
        """
        Retrieves an item corresponding to the searchkey

        preconditions: NonUniqueWrap is initialized
        postconditions: returns the item and True if retrieved, else (None, False)
        :return: item and True if retrieved, else (None, False)
        """
        item, succes = self.table.tableRetrieve(key)
        if not succes:
            return None, False
        else:
            return list(item.save())[0], True
