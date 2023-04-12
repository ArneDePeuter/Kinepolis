from kinepolis.Datastructuren.CEDRIC.DataTypes.BST import BST, TableItem


class Table:
    def __init__(self) -> None:
        self.datastruct = BST()

    def traverseTable(self, func):
        self.datastruct.inorderTraverse(func)

    # returns True if the ADT is empty
    def tableIsEmpty(self):
        self.datastruct.isEmpty()

    # Inserts an item into the ADT
    def tableInsert(self, key, val):
        self.datastruct.searchTreeInsert(TableItem(key, val))

    # Deletes an item from the ADT
    def tableDelete(self, key):
        self.datastruct.searchTreeDelete(key)

    # Retrieves an item from the ADT
    def tableRetrieve(self, key):
        self.datastruct.searchTreeRetrieve(key)
