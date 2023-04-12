from kinepolis.Datastructuren.ARNE.Datatypes.TwoThreeTree import TwoThreeTree, createItem


class TwoThreeTreeTable:
    # Initialisation 2-3 tree Table
    def __init__(self) -> None:
        self.ttt = TwoThreeTree()

    # Checks if the table is empty
    def tableIsEmpty(self):
        """
        Checks if the table is empty

        Pre-conditions: None
        Post-conditions: Returns True if the table is empty
        """
        return self.ttt.isEmpty()

    # Inserts a TableItem to the table
    def tableInsert(self, key, val):
        """
        Inserts to the table

        param key : key is the searchkey
        param val : value is the object

        Pre-conditions: None
        Post-conditions: The treeItem gets inserted to the table
        """
        return self.ttt.insertItem(createItem(key, val))

    # Retrieves an item from the table
    def tableRetrieve(self, key):
        """
        Retrieves an item from the table

        Pre-conditions: None
        Post-conditions: Returns a tuple (retrievedItem = item/None, done = True/False)
        """
        result, succes = self.ttt.retrieveItem(key)
        if result is not None:
            return result.val, succes
        else:
            return result, succes

    # Prints the table inorder
    def traverseTable(self, print):
        """
        Prints the table inorder

        Pre-conditions: None
        Post-conditions: prints the table inorder
        """
        self.ttt.inorderTraverse(print)

    # Deletes an item from the table
    def tableDelete(self, item):
        """
        Deletes an item from the table

        item is the target for deletion

        Pre-conditions: None
        Post-conditions: The given item gets deleted from the table
        """
        return self.ttt.deleteItem(item)
