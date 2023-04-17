from kinepolis.Datastructuren.ARNE.Datatypes.TwoThreeTree import TwoThreeTree as twoThreeTree, createItem

class TwoThreeTreeTable:
    def __init__(self, ttt=twoThreeTree) -> None:
        self.ttt = ttt()

    def traverseTable(self, func):
        self.ttt.inorderTraverse(func)

    # returns True if the ADT is empty
    def tableIsEmpty(self) -> bool:
        return self.ttt.isEmpty()

    # Inserts an item into the ADT
    def tableInsert(self, key, val) -> bool:
        return self.ttt.insertItem(createItem(key, val))

    # Deletes an item from the ADT
    def tableDelete(self, key) -> bool:
        return self.ttt.deleteItem(key)

    # Retrieves an item from the ADT
    def tableRetrieve(self, key) -> tuple:
        return self.ttt.retrieveItem(key)
