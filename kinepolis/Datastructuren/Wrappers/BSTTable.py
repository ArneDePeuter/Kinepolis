from kinepolis.Datastructuren.CEDRIC.DataTypes.BST import BST, TableItem

class BSTTable:
    def __init__(self, tree=BST()) -> None:
        self.datastruct = tree

    def traverseTable(self, func):
        self.datastruct.inorderTraverse(func)

    # returns True if the ADT is empty
    def tableIsEmpty(self) -> bool:
        return self.datastruct.isEmpty()

    # Inserts an item into the ADT
    def tableInsert(self, key, val) -> bool:
        return self.datastruct.searchTreeInsert(TableItem(key, val))

    # Deletes an item from the ADT
    def tableDelete(self, key) -> bool:
        return self.datastruct.searchTreeDelete(key)

    # Retrieves an item from the ADT
    def tableRetrieve(self, key) -> tuple:
        return self.datastruct.searchTreeRetrieve(key)
