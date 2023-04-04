from Datastructuren.CEDRIC.DataTypes.BST import BST, TreeItem


class BSTTable(BST):
    # Initialisation 2-3 tree Table
    def __init__(self) -> None:
        super().__init__()

    # Checks if the table is empty
    def tableIsEmpty(self):
        """
        Checks if the table is empty

        Pre-conditions: None
        Post-conditions: Returns True if the table is empty
        """
        return self.isEmpty()

    # Inserts a TreeItem to the table
    def tableInsert(self, key):
        """
        Inserts a TreeItem to the table

        TreeItem is of type twoThreeNode

        Pre-conditions: None
        Post-conditions: The treeItem gets inserted to the table
        """

        return self.retrieveItem(self.createItem(key, " ")).value

    # Retrieves an item from the table
    def tableRetrieve(self, item):
        """
        Retrieves an item from the table

        Pre-conditions: None
        Post-conditions: Returns a tuple (retrievedItem = item/None, done = True/False)
        """
        return self.searchTreeRetrieve(item)

    # Prints the table inorder
    def traverseTable(self, print):
        """
        Prints the table inorder

        Pre-conditions: None
        Post-conditions: prints the table inorder
        """
        self.inorderTraverse(print)

    # Deletes an item from the table
    def tableDelete(self, item):
        """
        Deletes an item from the table

        item is the target for deletion

        Pre-conditions: None
        Post-conditions: The given item gets deleted from the table
        """
        return self.searchTreeDelete(item)

    def createItem(self, key, val):
        return TreeItem(key, val)
